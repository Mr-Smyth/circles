import os
from flask import (
    Flask, flash, render_template,
    redirect, request, url_for)
from flask_pymongo import PyMongo

from bson.objectid import ObjectId
from werkzeug.security import (
    generate_password_hash, check_password_hash)

from helpers.utils import (
    call_search, get_parents, get_mothers_partners, get_fathers_partners,
    get_persons_data, build_target_list, merge_target_parent_list,
    link_real_siblings, get_selected_parents, get_chosen_parent,
    remove_all_links, remove_parent_link, choose_sibling_parents)

from helpers.create_update import (
    blank_template, call_person_update, call_create_person,
    create_parent)

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

#   SETUP env VARIABLES
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

#   SETUP INSTANCE OF PyMongo
mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    """ Home page view """
    return render_template("home.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    """ Search view

    Build and perform a search for whatever info user enters
    """
    # get search data and check for empty search
    if request.method == "POST":
        query = call_search()
        if len(query) > 0:
            people = list(mongo.db.people.find(query))
            error = "Sorry Circles has 0 records matching search.\
                Please use Add person to add this person"
        else:
            return redirect(url_for("home"))
    # return list of results and the error for no results.
    return render_template("home.html", people=people, error=error)



@app.route("/add_person/", methods=["GET", "POST"])
def add_person():
    """Add person view

    Creates a new person or updates in the case
    where user entered details match an existing person
    """
    if request.method == "POST":
        # Setup a person search to see if this person exists already
        person_search = call_search()
        if mongo.db.people.count_documents(person_search, limit=1) == 0:

            # person doesnt exist lets create them and insert
            person = call_create_person()
            person_inserted = mongo.db.people.insert_one(person)
            person_id = person_inserted.inserted_id
        else:
            # Person already exists - get and update them
            person_update = call_person_update()
            person_id = mongo.db.people.find_one(
                person_search)["_id"]
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(person_id)},
                {"$set": person_update})

        flash("This Person has been successfully added to Circles")
        return redirect(url_for(
            "assign_parents", person_id=person_id))

    families = mongo.db.family.find().sort("family_name", 1)
    return render_template(
        "add_person.html", families=families)


@app.route("/assign_parents/<person_id>", methods=["GET", "POST"])
def assign_parents(person_id):
    """ Assign parents view

    Display existing parents in the form inputs.
    Any name entered into the form will become the parent.
    In the case that name entered matches existing person, then existing
    person becomes the parent.
    In the case where there is an existing parent and the user changes the
    details a check is done to see if that matches an existing person, if
    so then that person becomes the new parent. Otherwise the existing
    parent is edited.
    Also make sure parents are connected as spouse/partners.

    Args:
        person_id (str): The id of the person being edited.
    """
    # Required variables
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    persons_id = person["_id"]
    mother_id = person["parents"]["mother"]
    father_id = person["parents"]["father"]
    mother_entered = False
    father_entered = False
    both_parents = False

    # Check if parents exist to decide if to allow skipping of this stage
    # Also to provide parent info to the rendered template
    if mother_id != "":
        existing_mother = mongo.db.people.find_one({
            "_id": ObjectId(mother_id)
            })
        mother_entered = True
    else:
        existing_mother = blank_template()
    if father_id != "":
        existing_father = mongo.db.people.find_one({
            "_id": ObjectId(father_id)
            })
        father_entered = True
    else:
        existing_father = blank_template()
    if mother_entered and father_entered:
        both_parents = True
    else:
        both_parents = False

    if request.method == "POST":
        # Remove person from any child array. dont want person being
        # a child of 2 mothers - parents are reassigned later
        mongo.db.people.update({}, {"$pull": {
             "children": {"$in": [persons_id]}}}, multi=True)

        # Get mother and father from form
        mother = {
            "first_name": request.form.get(
                "mothers_first_name").lower().strip(),
            "last_name": request.form.get("mothers_last_name").lower().strip(),
            "dob": request.form.get("mothers_dob")
        }
        father = {
            "first_name": request.form.get(
                "fathers_first_name").lower().strip(),
            "last_name": request.form.get("fathers_last_name").lower().strip(),
            "dob": request.form.get("fathers_dob")
        }

        # Check for mother
        if mongo.db.people.count_documents(mother, limit=1) == 0:
            # No match in db - so we will edit current mother
            if mother_entered:
                mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(mother_id)},
                    {"$set": mother})
            else:
                # No found or existing mother - create one and add child
                mother = create_parent(person, 'mother')
                mongo.db.people.insert_one(mother)
                mother_id = mongo.db.people.find_one(mother)["_id"]
                mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(mother_id)},
                    {"$addToSet": {"children": persons_id}})

        else:
            # Here we have a match for mother - so update her
            found_mother = mongo.db.people.find_one(mother)["_id"]
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(found_mother)},
                {"$addToSet": {"children": persons_id}})
            mother_id = found_mother

        # Check for father
        if mongo.db.people.count_documents(father, limit=1) == 0:
            # No match in db - so we will edit current father
            if father_entered:
                mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(father_id)},
                    {"$set": father})
            else:
                # No found or existing father - create one and add child
                father = create_parent(person, 'father')
                mongo.db.people.insert_one(father)
                father_id = mongo.db.people.find_one(father)["_id"]
                mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(father_id)},
                    {"$addToSet": {"children": persons_id}})

        else:
            # Here we have a match for father - so update her
            found_father = mongo.db.people.find_one(father)["_id"]
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(found_father)},
                {"$addToSet": {"children": persons_id},
                 "$set": father})
            father_id = found_father

        # Update persons parents and make parents partners of eachother
        parents = {"mother": mother_id, "father": father_id}
        mongo.db.people.find_one_and_update(
            {"_id": ObjectId(person_id)}, {"$set": {"parents": parents}})
        mongo.db.people.find_one_and_update(
            {"_id": ObjectId(mother_id)},
            {"$addToSet": {"spouse_partner": father_id}})
        mongo.db.people.find_one_and_update(
            {"_id": ObjectId(father_id)},
            {"$addToSet": {"spouse_partner": mother_id}})

        flash("Circle has been updated")
        return redirect(url_for("assign_spouse_partner", person_id=person_id))

    return render_template(
        "assign_parents.html", existing_mother=existing_mother,
        existing_father=existing_father, person=person,
        both_parents=both_parents)


@app.route("/assign_spouse_partner/<person_id>", methods=["GET", "POST"])
def assign_spouse_partner(person_id):
    """ Spouse / Partner View

    Pass current spouse / partners of person to template
    Handle adding of Spouse/Partners.

    Args:
        person_id (str): The id of the person being edited.
    """
    # Req Variables
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    persons_id = person["_id"]

    # Grab existing Spouse/Partners for the template
    existing_spouse_partners = get_persons_data(person, 'spouse_partner')

    if request.method == "POST":
        # Build a search and see if entered Spouse/partner exists
        spouse_partner_search = call_search()
        if mongo.db.people.count_documents(
                spouse_partner_search, limit=1) == 0:

            # Dont exist - so create them and insert them
            # then make them partners of eachother
            spouse_partner = call_create_person(person)
            mongo.db.people.insert_one(spouse_partner)
            new_spouse_partner_id = mongo.db.people.find_one(
                spouse_partner)["_id"]
            mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(new_spouse_partner_id)},
                    {"$addToSet": {"spouse_partner": persons_id}})
            mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(person_id)},
                    {"$addToSet": {"spouse_partner": new_spouse_partner_id}})

        else:
            # Entered Spouse/Partner does exist - So get them
            # then make them partners of eachother
            found_spouse_partner = mongo.db.people.find_one(
                spouse_partner_search)
            found_spouse_partner_id = found_spouse_partner["_id"]
            mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(found_spouse_partner_id)},
                    {"$addToSet": {"spouse_partner": persons_id}})
            mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(persons_id)},
                    {"$addToSet": {"spouse_partner": found_spouse_partner_id}})

        flash("Circle has been updated")
        return redirect(url_for(
            "assign_spouse_partner", person_id=person_id))

    return render_template(
        "assign_spouse_partner.html",
        existing_spouse_partners=existing_spouse_partners, person=person)


@app.route("/assign_siblings/<person_id>", methods=["GET", "POST"])
def assign_siblings(person_id):
    """ Assign Siblings View

    Gets persons parents and partners and passes to template.
    Gets persons siblings and passes to template.
    Gets siblings info ready for comparison/assigning to each sibling.
    Handle assigning of a new sibling from form entry.

    Args:
        person_id (str): The id of the person being edited.
    """
    # Some Required Variables
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    # Get parents and partners for template.
    persons_parents = get_parents(person)
    mothers_partners_list = get_mothers_partners(person, persons_parents)
    fathers_partners_list = get_fathers_partners(person, persons_parents)
    # Get existing Siblings for template
    existing_siblings = get_persons_data(person, 'siblings')
    # Build a list of siblins and parents for later comparison
    sibling_and_parent_list = build_target_list(person, 'siblings')

    if request.method == "POST":
        # Get the parent selection by user
        selected_parents = choose_sibling_parents(persons_parents)

        # Build a search for user entered sibling and search
        sibling_search = call_search()
        if mongo.db.people.count_documents(sibling_search, limit=1) == 0:
            # They dont exist - so create them
            sibling = call_create_person(person, selected_parents)
            mongo.db.people.insert_one(sibling)
            new_sibling_id = mongo.db.people.find_one(sibling)["_id"]

            # Update parents - check if any parent is blank first
            if any(value != "" for value in selected_parents.values()):
                for key, value in selected_parents.items():
                    mongo.db.people.find_one_and_update(
                        {"_id": ObjectId(value)}, {"$addToSet": {
                            "children": new_sibling_id}})

            # Update persons siblings:
            mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(person_id)},
                    {"$addToSet": {"siblings": new_sibling_id}})
            # Update new sibling with the id of each existing sibling of person
            for sibling_element in sibling_and_parent_list:
                mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(new_sibling_id)}, {"$addToSet": {
                        "siblings": sibling_element[0]}})
            # Update each existing sibling of person with new sibling
            for sibling_element in sibling_and_parent_list:
                mongo.db.people.find_one_and_update(
                    {"_id": sibling_element[0]}, {"$addToSet": {
                        "siblings": new_sibling_id}})

        else:
            # Sibling does exist so get them and update:
            found_sibling = mongo.db.people.find_one(sibling_search)
            found_sibling_id = found_sibling["_id"]

            """ I Remove the found sibling from any children array because im
            assigning parents and i dont want someone with 2 mothers.
            Also, I remove the found sibling id from any sibling
            Array - this is in case the parents are changing
            Siblings will be reassigned, if at least on parent matches
            """
            mongo.db.people.update({}, {"$pull": {
             "children": {"$in": [found_sibling_id]}}}, multi=True)
            mongo.db.people.update({}, {"$pull": {
             "sibling": {"$in": [found_sibling_id]}}}, multi=True)

            # Update found sibling and the selected parents
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(found_sibling_id)},
                {"$set": {"parents": selected_parents}})
            if any(x != "" for x in selected_parents.values()):
                for key, value in selected_parents.items():
                    mongo.db.people.find_one_and_update(
                        {"_id": ObjectId(value)}, {"$addToSet": {
                            "children": found_sibling_id}})

            # get siblings of found sibling and add to list
            found_siblings_of_sibling = found_sibling["siblings"]
            found_siblings_of_sibling.insert(0, found_sibling_id)

            # Build a combined sibling list and link only valid siblings
            full_sibling_parent_list = merge_target_parent_list(
                found_siblings_of_sibling, sibling_and_parent_list)
            link_real_siblings(full_sibling_parent_list)

        flash("Circle has been updated")
        return redirect(url_for(
            "assign_siblings", person_id=person_id))

    return render_template(
        "assign_siblings.html", existing_siblings=existing_siblings,
        persons_parents=persons_parents,
        mothers_partners_list=mothers_partners_list,
        fathers_partners_list=fathers_partners_list, person=person)


@app.route("/check_if_partner_exists/<person_id>")
def check_if_partner_exists(person_id):
    """ Check if there is any partners linked to person view

    If there is an existing spouse/partner then allow continue to Assign
    Children.
    If no partner exists then do not allow continue to Assign Children.

    Args:
        person_id (str): The id of the person being edited.
    """

    # Required variables
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    persons_spouse_partner_ids = person["spouse_partner"]

    if len(persons_spouse_partner_ids) > 0:
        return redirect(url_for(
            "assign_children", person_id=person_id))

    return render_template("check_if_partner_exists.html", person=person)


@app.route("/assign_children/<person_id>", methods=["GET", "POST"])
def assign_children(person_id):
    """ Assign children view

    Get the persons children information and passes to template.
    Get the persons partners and pass them to the template.
    Gets siblings info ready for comparison/assigning to each sibling.
    Handle adding of new child by user.

    Args:
        person_id (str): The id of the person being edited.
    """

    # Required variables
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    persons_id = person["_id"]

    # Get existing children for template
    existing_children = get_persons_data(person, 'children')
    # Get persons partners for template - for parent selection
    persons_spouse_partners = get_persons_data(person, 'spouse_partner')
    # Build a list of children and parents for later comparison
    children_and_parent_list = build_target_list(person, 'children')

    if request.method == "POST":
        # Get parents - person and other selected parents details
        child_parents = get_selected_parents(person, persons_spouse_partners)
        selected_parent = get_chosen_parent(persons_spouse_partners)

        # Get the other parents children - update children_and_parent_list
        selected_parent_children = build_target_list(
            selected_parent, 'children')
        for group in selected_parent_children:
            if group not in children_and_parent_list:
                children_and_parent_list.append(group)

        # Search for user entered child
        child_search = call_search()
        if mongo.db.people.count_documents(child_search, limit=1) == 0:
            # Child does not exist - create and Update parents with new child
            child = call_create_person(person, child_parents)
            mongo.db.people.insert_one(child)
            child_id = mongo.db.people.find_one(child)["_id"]
            if any(value != "" for value in child_parents.values()):
                for key, value in child_parents.items():
                    mongo.db.people.find_one_and_update(
                        {"_id": ObjectId(value)}, {"$addToSet": {
                            "children": child_id}})

            # Each child of parents will be a sibling of the new child
            for child_element in children_and_parent_list:
                mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(child_id)}, {"$addToSet": {
                        "siblings": child_element[0]}})
            # Each child of parents has a new sibling that is - the new child
            for child_element in children_and_parent_list:
                mongo.db.people.find_one_and_update(
                    {"_id": child_element[0]}, {"$addToSet": {
                        "siblings": ObjectId(child_id)}})

        else:
            # Then Child does exist
            found_child = mongo.db.people.find_one(child_search)
            child_id = found_child["_id"]

            """ Here i delete found child from any siblings array and
            from any siblings array - they will be reassigned correct ones
            once parents are assigned  """
            mongo.db.people.update({}, {"$pull": {
                "siblings": {"$in": [child_id]}}}, multi=True)
            mongo.db.people.update({}, {"$pull": {
                "children": {"$in": [child_id]}}}, multi=True)

            # Assign parents to child and update parents with new child
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(child_id)},
                {"$set": {"parents": child_parents}})
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(persons_id)},
                {"$addToSet": {"children": child_id}})
            # check in case parent not present.
            if selected_parent['_id']:
                mongo.db.people.find_one_and_update(
                    {"_id": selected_parent['_id']},
                    {"$addToSet": {"children": child_id}})

            # Update children_and_parent_list with siblings of found child
            found_siblings_of_child = found_child["siblings"]
            found_siblings_of_child.insert(0, child_id)

            # Build a combined sibling list and link only valid siblings
            full_sibling_parent_list = merge_target_parent_list(
                found_siblings_of_child, children_and_parent_list)
            link_real_siblings(full_sibling_parent_list)

        flash("Circle has been updated")
        return redirect(url_for("assign_children", person_id=person_id))

    return render_template(
        'assign_children.html',
        persons_spouse_partners=persons_spouse_partners,
        existing_children=existing_children, person=person)


@app.route(
    "/manage_partner_relationship/<person_id>/<person2_id>")
def manage_partner_relationship(person_id, person2_id):
    """ Manage Spouse/Partner relationship

    Decides if partners should be allowed to unlink, depending
    on if they have a common child.
    Returns choice to template for user to decide.

    Args:
        person_id (str): The id of the person being edited.
        person2_id (str): The id of the Partner/Spouse.
    """

    # Required Variables
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    person2 = mongo.db.people.find_one({"_id": ObjectId(person2_id)})
    partner_children = person2['children']
    person_children = person['children']
    unlink = False
    message = ""

    # If they have a common child do not allow unlink. Else - allow.
    if len(person_children) > 0:
        check = any(
            item in person_children for item in partner_children)
        if check is True:
            unlink = False
        else:
            unlink = True
    else:
        unlink = True

    return render_template(
        "manage_partner_relationship.html", unlink=unlink, person2=person2,
        person=person, message=message)


@app.route(
    "/delete_partner_relationship/<person_id>/<person2_id>")
def delete_partner_relationship(person_id, person2_id):
    """ Remove a spouse / partner

    Handles the unlinking of spouse partners.

    Args:
        person_id (str): The id of the person being edited.
        person2_id (str): The id of the Partner/Spouse.
    """
    #   Required variables
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    person2 = mongo.db.people.find_one({"_id": ObjectId(person2_id)})
    partners_id = person2['_id']
    persons_id = person['_id']

    mongo.db.people.update({"_id": ObjectId(partners_id)}, {
        "$pull": {"spouse_partner": {"$in": [persons_id]}}})
    mongo.db.people.update({"_id": ObjectId(persons_id)}, {
        "$pull": {"spouse_partner": {"$in": [partners_id]}}})

    flash("Spouse / Partner relationship has been removed")
    return redirect(url_for(
            "assign_spouse_partner", person_id=person_id))


@app.route(
    "/manage_sibling_relationship/<person_id>/<person2_id>")
def manage_sibling_relationship(person_id, person2_id):
    """ Manage Sibling relationship view

    View that acts as a buffer for removing siblings,
    reminds the user what they are doing and provides options.

    Args:
        person_id (str): The id of the person being edited.
        person2_id (str): The id of the sibling.
    """
    # Required variables
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    person2 = mongo.db.people.find_one({"_id": ObjectId(person2_id)})

    return render_template(
        "manage_sibling_relationship.html", person2=person2,
        person=person)


@app.route(
    "/delete_sibling_relationship/<person_id>/<person2_id>",
    methods=["GET", "POST"])
def delete_sibling_relationship(person_id, person2_id):
    """ Remove Sibling relationship view

    Handle removal of a sibling of person

    Args:
        person_id (str): The id of the person being edited.
        person2_id (str): The id of the Sibling.
    """
    # Required variables
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})['_id']
    sibling = mongo.db.people.find_one({"_id": ObjectId(person2_id)})['_id']

    mongo.db.people.update({"_id": ObjectId(person)}, {
        "$pull": {"siblings": {"$in": [sibling]}}})
    mongo.db.people.update({"_id": ObjectId(sibling)}, {
        "$pull": {"siblings": {"$in": [person]}}})

    flash("Sibling relationship has been removed")
    return redirect(url_for(
            "assign_siblings", person_id=person_id))


@app.route("/manage_child_relationship/<person_id>/<person2_id>")
def manage_child_relationship(person_id, person2_id):
    """ Manage Child relationship view

    View that acts as a buffer for removing Children,
    reminds the user what they are doing and provides options.

    Args:
        person_id (str): The id of the person being edited.
        person2_id (str): The id of the Child.
    """
    # Required variables
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    person2 = mongo.db.people.find_one({"_id": ObjectId(person2_id)})

    return render_template(
        "manage_child_relationship.html", person2=person2,
        person=person)


@app.route(
    "/delete_child_relationship/<person_id>/<person2_id>",
    methods=["GET", "POST"])
def delete_child_relationship(person_id, person2_id):
    """ Remove Child relationship view

    Handle removal of a child of person

    Args:
        person_id (str): The id of the person being edited.
        person2_id (str): The id of the child.
    """
    # Required variables
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    person_id = person['_id']
    child = mongo.db.people.find_one({"_id": ObjectId(person2_id)})
    child_id = child['_id']
    child_parents = child['parents']

    # remove person as a parent - get which parent person is
    removed_parent_gender = person['gender']
    if removed_parent_gender == 'male':
        child_parents['father'] = ""
    else:
        child_parents['mother'] = ""

    mongo.db.people.update({"_id": ObjectId(person_id)}, {
        "$pull": {"children": {"$in": [child_id]}}})
    mongo.db.people.find_one_and_update(
                {"_id": ObjectId(child_id)},
                {"$set": {"parents": child_parents}})

    flash("Children relationship has been removed")
    return redirect(url_for(
            "assign_children", person_id=person_id))

    return render_template("assign_spouse_partner.html", person_id=person_id)


@app.route("/edit_person/<person_id>", methods=["GET", "POST"])
def edit_person(person_id):
    """ Edit person view

    Pass person information to the template
    Check if any updates match an existing person, if they do
    then they will be notified, if not make update

    Args:
        person_id (str): The id of the person being edited.
    """
    # Required variables
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    families = mongo.db.family.find().sort("family_name", 1)

    if request.method == "POST":
        # Build a search
        person_search = call_search()

        # build an update for person
        person_update = call_person_update()

        # Checking to see if person exists
        if mongo.db.people.count_documents(person_search, limit=1) == 0:
            # Person does not exist - update person
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(person_id)},
                {"$set": person_update})

            flash("Circle has been updated")
            return redirect(url_for(
                "assign_parents", person_id=person_id))
        else:
            # Person exists - check if they are same person - if yes - update
            duplicate_id = mongo.db.people.find_one(
                person_search)['_id']
            person_id = mongo.db.people.find_one(
                {"_id": ObjectId(person_id)})['_id']
            if duplicate_id == person_id:
                mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(person_id)},
                    {"$set": person_update})

                flash("Circle has been updated")
                return redirect(url_for(
                    "assign_parents", person_id=person_id))

            # Then there is a conflict with another person - notify user
            return redirect(url_for("notify_duplicate", person_id=person_id,
                                    duplicate_id=duplicate_id))
    return render_template(
        "edit_person.html", person=person, families=families)


@app.route("/notify_duplicate/<person_id>/<duplicate_id>")
def notify_duplicate(person_id, duplicate_id):
    """ Notify Duplicates view

    Notify user that person edited results in a duplicate

    Args:
        person_id (str): The id of the person being edited.
        duplicate_id (str): The id of the person found to be a duplicate.
    """
    # Required variables
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    duplicate = mongo.db.people.find_one({"_id": ObjectId(duplicate_id)})

    return render_template(
        "notify_duplicate.html", person=person, duplicate=duplicate)


@app.route("/view_circle/<person_id>")
def view_circle(person_id):
    """ View Circle view

    Pass alll user relationships to template

    Args:
        person_id (str): The id of the person being viewed.

    """
    # Required variables
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    persons_mother = person["parents"]["mother"]
    persons_father = person["parents"]["father"]
    mother = {}
    father = {}
    spouse_partner = person['spouse_partner']
    spouse_partner_list = []
    siblings = person['siblings']
    siblings_list = []
    children = person['children']
    children_list = []

    # Get persons parents
    if persons_mother != "":
        mother = mongo.db.people.find_one({
            "_id": ObjectId(persons_mother)
            })
    if persons_father != "":
        father = mongo.db.people.find_one({
            "_id": ObjectId(persons_father)
            })

    # Get the Spouse/partners, Siblings and children
    for partner in spouse_partner:
        spouse_partner_list.append(mongo.db.people.find_one({
            "_id": ObjectId(partner)
            }))
    for sibling in siblings:
        siblings_list.append(mongo.db.people.find_one({
            "_id": ObjectId(sibling)
            }))
    for child in children:
        children_list.append(mongo.db.people.find_one({
            "_id": ObjectId(child)
            }))

    return render_template(
        "view_circle.html", person=person, mother=mother, father=father,
        spouse_partner_list=spouse_partner_list, siblings_list=siblings_list,
        children_list=children_list)


@app.route("/manage_people", methods=["GET", "POST"])
def manage_people():
    """ Manage people view

    Handle search element of delete a person in the manage people view

    """
    people = {}
    error = ""
    if request.method == "POST":
        # Build query from form and search
        query = call_search()

        if len(query) > 0:
            people = list(mongo.db.people.find(query))
            error = "Sorry we have no records matching your query."
        else:
            return redirect(url_for("manage_people"))

    return render_template("manage_people.html", people=people, error=error)


@app.route("/delete_person/<person_id>", methods=["GET", "POST"])
def delete_person(person_id):
    """ Delete a person function

    Handle deletion of a person and the removal of any relationships

    Args:
        person_id (str): The id of the person being deleted.
    """
    # Required variables
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    persons_id = person["_id"]

    # Remove person
    remove_all_links(persons_id)
    remove_parent_link(person)

    flash("Person has been successfully removed from Circles")

    return render_template("manage_people.html")


@app.route("/delete_all_documents", methods=["GET", "POST"])
def delete_all_documents():
    """ Delete all documents:

    Remove everyone if correct deletion password was entered.

    """
    # check password - if good - delete all documents
    if check_password_hash(
            mongo.db.users.find_one(
                {'user_name': 'validation'})["del_password"],
            request.form.get("password")):
        mongo.db.people.remove({})
        flash("Circles has been Deleted")
        return redirect(url_for("manage_people"))
    else:
        flash("The password you entered was incorrect.\
            Circles has not been Deleted.")

    return render_template("manage_people.html")


@app.route("/change_password", methods=["GET", "POST"])
def change_password():
    """ Remove Password:

    Handle changing of deletion password

    """
    if request.method == "POST":
        # Check if existing password is correct
        if check_password_hash(
            mongo.db.users.find_one(
                {'user_name': 'validation'})["del_password"], request.form.get(
                    "existing_password")):
            # Check to see if new passwords match
            password1 = request.form.get("new_password")
            password2 = request.form.get("repeat_new_password")
            if password1 == password2:
                new_password = {
                    'del_password': generate_password_hash(
                        request.form.get("new_password"))
                }
                # Update password
                mongo.db.users.find_one_and_update(
                    {"user_name": "validation"}, {"$set": new_password})

                flash("The password has been updated")

        else:
            flash("The password you entered did not match.\
                The Password has not been changed")

    return render_template("manage_people.html")


@app.errorhandler(404)
def page_not_found(e):
    """ Handle 404 error """
    return render_template("404.html")


@app.errorhandler(500)
def server_error(e):
    """ Handle 500 error """
    return render_template("500.html")


# How to run this application
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
