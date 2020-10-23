import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo

from bson.objectid import ObjectId
from werkzeug.security import (
    generate_password_hash, check_password_hash)

from utils import (
    call_search, get_parents, get_mothers_partners, get_fathers_partners,
    get_persons_data, build_target_list, merge_target_parent_list,
    link_real_siblings, get_selected_parents, get_chosen_parent,
    remove_all_links, remove_parent_link, choose_sibling_parents)

from create_update import (
    blank_template, call_person_update, call_create_person,
    create_parent)

# Import env.py if it exists
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

#   SETUP OUR env VARIABLES
#   MONGO DBNAME
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
#   GET THE MONGO URI OR CONNECTION STRING
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
#    GET THE SECRET KEY WHICH IS REQUIRED FOR PARTS OF FLASK, LIKE FLASH
app.secret_key = os.environ.get("MONGO_DBNAME")

#   SETUP INSTANCE OF PyMongo AND ADD IN app.py
mongo = PyMongo(app)


#   BASE ROUTE
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


#   SEARCH VIEW
@app.route("/search", methods=["GET", "POST"])
def search():

    #   FUNCTION PURPOSE -
    #   TO BUILD A SEARCH QUERY FROM WHATEVER THE USER CHOOSES TO
    #       ENTER AND RUN THE SEARCH AND RETURN RESULTS

    if request.method == "POST":

        query = call_search()

        #   CHECK IF THE QUERY IS NOT BLANK - SOMEONE JUST CLICKED
        #       SEARCH WITHOUT ANY ENTRIES?
        if len(query) > 0:
            people = list(mongo.db.people.find(query))
            error = "Sorry we have no records matching your query."
        else:
            return redirect(url_for("home"))

        # RETURN TO HOME, THE RESULTS CURSOR
    return render_template("home.html", people=people, error=error)


#   ADD PERSON VIEW
@app.route("/add_person/", methods=["GET", "POST"])
def add_person():

    #   FUNCTION PURPOSE -
    # 1.    GETS INFORMATION FROM THE FORM AND CREATES A NEW
    #       PERSON IN CIRCLES
    # 2.    IF PERSON ENTERED EXISTS - THEN PERSON WILL NOT BE DUPLICATED
    #       AND ANY EXTRA INFORMATION WILL BE UPDATED TO THE EXISTING PERSON

    if request.method == "POST":
        #   GET CALL_SEARCH RESULT QUERY
        person_search = call_search()

        #   CHECK TO SEE IF PERSON ALREADY EXISTS
        if mongo.db.people.count_documents(person_search, limit=1) == 0:

            #   GET A TEMPLATE FOR IMPORTING NEW PERSON
            person = call_create_person()
            #   ADD THE PERSON DICTIONARY TO MONGO AND GET THE ID BACK
            person_inserted = mongo.db.people.insert_one(person)
            person_id = person_inserted.inserted_id
        else:

            #   THEN PERSON ALREADY EXISTS, WE CAN UPDATE THEM
            #   GET TEMPLATE FOR UPDATING EXISTING PERSON
            person_update = call_person_update()
            person_id = mongo.db.people.find_one(
                person_search)["_id"]
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(person_id)},
                {"$set": person_update})

        flash("This Person has been successfully added to Circles")
        return redirect(url_for(
            "assign_parents", person_id=person_id))

    # GET THE FAMILY COLLECTION NAMES, FOR THE FAMILY
    # SELECTION DROP DOWN
    families = mongo.db.family.find().sort("family_name", 1)
    # RETURN THE FAMILIES TO THE ADD_PERSON PAGE FOR JINGA
    return render_template(
        "add_person.html", families=families)


#   ASSIGN PARENTS VIEW
@app.route("/assign_parents/<person_id>", methods=["GET", "POST"])
def assign_parents(person_id):

    # FUNCTION PURPOSE -
    # 1.    GET AND DISPLAY EXISTING PARENTS IN FORM.
    # 2.    ANY NEW NAME ENTERED IN FORM WILL BECOME THE NEW PARENT - IT
    #       DOES NOT EDIT EXISTING PARENT, IT SEARCHES TO SEE IF THE PARENT
    #       EXISTS, IF YES, THEN THEY ARE UPDATED AS A PARENT OF THE PERSON
    #       BEING EDITED, OTHERWISE THEY ARE CREATED.
    # 3.    IT ALSO MAKES SURE THAT THE 2 PARENTS ARE CONNECTED AS
    #       SPOUSE_PARTNER AS THEY HAVE A RELEVANT RELATIONSHIP DUE TO HAVING
    #       A CHILD.

    #   SETUP REQUIRED VARIABLES
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    persons_id = person["_id"]
    persons_mother_id = person["parents"]["mother"]
    persons_father_id = person["parents"]["father"]
    mother_entered = False
    father_entered = False
    both_parents = False

    #   PREP FOR RENDER TEMPLATE -
    #   PERSONS MOTHER - CHECK IF MOTHER ALREADY LINKED
    if persons_mother_id != "":
        #   THEN IT HAS EXISTING MOTHER - SO ASSIGN THE ID
        existing_mother = mongo.db.people.find_one({
            "_id": ObjectId(persons_mother_id)
            })
        mother_entered = True
    else:
        #   ITS A NEW MOTHER - NO TEMPLATE YET
        #   SO WE GIVE IT ONE
        existing_mother = blank_template()

    #   PERSONS FATHER - CHECK IF FATHER ALREADY LINKED
    if persons_father_id != "":
        #   THEN IT HAS EXISTING FATHER - SO ASSIGN THE ID
        existing_father = mongo.db.people.find_one({
            "_id": ObjectId(persons_father_id)
            })
        father_entered = True
    else:
        #   ITS A NEW FATHER - NO TEMPLATE YET
        #   SO WE GIVE IT ONE
        existing_father = blank_template()

    # IM USING THIS VARIABLE TO EITHER ALLOW OR
    # NOT ALLOW THE NEXT BUTTON
    if mother_entered and father_entered:
        both_parents = True
    else:
        both_parents = False

    #   WHEN FORM IS SUBMITTED / UPDATED
    if request.method == "POST":

        #   IMPORTANT - WE REMOVE THE PERSONS ID FROM ANY CHILDREN
        #   ARRAY - THIS IS BECAUSE WE ARE POSTING NEW PARENTS.
        #   WE DONT WANT PERSON HAVING 2 BIRTH MOTHERS.
        mongo.db.people.update({}, {"$pull": {
             "children": {"$in": [persons_id]}}}, multi=True)

        #   GET THE TEMPLTE FROM THE FORM
        #   FOR MOTHER
        mother = {
            "first_name": request.form.get(
                "mothers_first_name").lower().strip(),
            "last_name": request.form.get("mothers_last_name").lower().strip(),
            "dob": request.form.get("mothers_dob")
        }
        #   FOR FATHER
        father = {
            "first_name": request.form.get(
                "fathers_first_name").lower().strip(),
            "last_name": request.form.get("fathers_last_name").lower().strip(),
            "dob": request.form.get("fathers_dob")
        }

        #   FIRST WE CHECK IF MOTHER EXISTS ANYWHERE IN THE DB
        if mongo.db.people.count_documents(mother, limit=1) == 0:
            #   IF THE COUNT IS == O, THEN WE INSERT A NEW MOTHER
            # BUILD A NEW MOTHER OBJECT
            mother = create_parent(person, 'mother')

            #   INSERT THE NEW MOTHER, THEN GET BACK THE ID
            mongo.db.people.insert_one(mother)
            mother_id = mongo.db.people.find_one(mother)["_id"]

            # ADD THE PERSON TO THEIR NEW MOTHER AS A CHILD
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(mother_id)},
                {"$addToSet": {"children": persons_id}})

        else:
            #   IF THE COUNT IS NOT == O, THEN WE HAVE A MATCH FOR MOTHER
            #   SO WE UPDATE THAT MOTHER WITH THEIR NEW CHILD
            found_mother = mongo.db.people.find_one(mother)["_id"]
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(found_mother)},
                {"$addToSet": {"children": persons_id}})
            mother_id = found_mother

        #   NEXT WE CHECK IF FATHER EXISTS ANYWHERE IN THE DB
        if mongo.db.people.count_documents(father, limit=1) == 0:
            #   IF THE COUNT IS == O, THEN WE INSERT A NEW FATHER
            # BUILD A NEW FATHER OBJECT
            father = create_parent(person, 'father')

            #   INSERT THE NEW FATHER, THEN GET BACK THE ID
            print("======================================")
            print(father)
            mongo.db.people.insert_one(father)
            father_id = mongo.db.people.find_one(father)["_id"]

            # ADD THE PERSON TO THEIR NEW FATHER AS A CHILD
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(father_id)},
                {"$addToSet": {"children": persons_id}})

        else:
            #   IF THE COUNT IS NOT == O, THEN WE HAVE A MATCH FOR FATHER
            #   SO WE UPDATE THAT FATHER WITH THEIR NEW CHILD
            found_father = mongo.db.people.find_one(father)["_id"]
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(found_father)},
                {"$addToSet": {"children": persons_id},
                 "$set": father})
            father_id = found_father

        #   HERE WE BUILD THE PARENTS INTO A DICT AND SET IT INSIDE THE PERSON
        # AS PARENTS
        parents = {"mother": mother_id, "father": father_id}
        mongo.db.people.find_one_and_update(
            {"_id": ObjectId(person_id)}, {"$set": {"parents": parents}})

        #   WE ALSO NEED TO ADD THE PARENTS AS A SPOUSE / PARTNERS OF
        #   EACH OTHER, BECAUSE THEY HAVE A SIGNIFICANT RELATIONSHIP
        #   DUE TO HAVING A CHILD TOGETHER
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


# TO HANDLE ADDING A SPOUSE/PARTNER VIEW
@app.route("/assign_spouse_partner/<person_id>", methods=["GET", "POST"])
def assign_spouse_partner(person_id):

    # SETUP SOME REQUIRED VARIABLES
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    persons_id = person["_id"]

    # GET EXISTING SPOUSE_PARTNERS TO RETURN TO TEMPLATE FOR DISPLAYING
    existing_spouse_partners = get_persons_data(person, 'spouse_partner')

    if request.method == "POST":
        # BUILD A SEARCH OBJECT FROM DATA IN THE FORM
        spouse_partner_search = call_search()

        # SEE IF PERSON ENTERED ON FORM EXISTS
        if mongo.db.people.count_documents(
                spouse_partner_search, limit=1) == 0:

            # GET A SPOUSE/PARTNER OBJECT TO CREATE THIS PERSON
            spouse_partner = call_create_person(person)

            # INSERT THE NEW SPOUSE/PARTNER THEN GET ID IN CORRECT FORMAT
            mongo.db.people.insert_one(spouse_partner)
            new_spouse_partner_id = mongo.db.people.find_one(
                spouse_partner)["_id"]

            # ADD PERSON AS A SPOUSE/PARTNER OF THE NEW SPOUSE/PARTNER
            mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(new_spouse_partner_id)},
                    {"$addToSet": {"spouse_partner": persons_id}})

            # UPDATE PERSON WITH THE NEW SPOUSE/PARTNER
            mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(person_id)},
                    {"$addToSet": {"spouse_partner": new_spouse_partner_id}})

        else:
            # ELSE THE SPOUSE/PARTNER DOES EXIST IN DB
            # SO WE FIND THEM
            found_spouse_partner = mongo.db.people.find_one(
                spouse_partner_search)
            found_spouse_partner_id = found_spouse_partner["_id"]

            # ADD PERSONS ID TO FOUND SPOUSE_PARTNER
            mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(found_spouse_partner_id)},
                    {"$addToSet": {"spouse_partner": persons_id}})

            # ADD FOUND SPOUSE / PARTNER TO PERSON
            mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(persons_id)},
                    {"$addToSet": {"spouse_partner": found_spouse_partner_id}})

        flash("Circle has been updated")
        return redirect(url_for(
            "assign_spouse_partner", person_id=person_id))

    return render_template(
        "assign_spouse_partner.html",
        existing_spouse_partners=existing_spouse_partners, person=person)


# TO HANDLE ADDING OF A SIBLING VIEW
@app.route("/assign_siblings/<person_id>", methods=["GET", "POST"])
def assign_siblings(person_id):

    # FUNCTION PURPOSE -
    # 1.    GETS THE PERSONS SIBLING INFORMATION AND DISPLATS IT WITHIN
    #       THE TEMPLATE.
    # 2.    GETS THE SIBLINGS INFO AND GETS IT READY TO BE COMPARED WHEN
    #       POSTING
    #       THIS WAS TO SOLVE A SCALING ISSUE WHERE WHEN I TRIED TO ADD 10
    #       SIBLINGS THE SYSTEM TIMED OUT, IT WAS DOING TO MUCH IN THE
    #       POST SECTION, AS IT HAD TO CHECK EVERY SIBLING AND CHECK IF AT
    #       LEAST ONE PARENT MATCHED.
    # AFTER POST -
    # 1.    SEARCH FOR THE SIBLING ENTERED FROM THE FORM GRAB PARENTS FROM
    #       THE FORM
    # 2.    IF SIBLING DOES NOT EXIST - CREATE IT, LINK ITS SIBLINGS,
    #       UPDATE OTHER SIBLINGS, PARENTS AND INSERT INTO PARENTS AS A CHILD
    # 3.    ELSE IF THE SIBLING DOES EXIST:
    #       - CHECK FOR MATCHING PARENTS.
    #       - LINK IT TO ITS NEW SIBLINGS.
    #       - UPDATE ITS NEW & OLD SIBLINGS.
    #       - UPDATE PARENTS AND UPDATE NEW AND OLD PARENTS CHILDREN

    # SETUP SOME REQUIRED VARIABLES
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})

    # I NEED TO SEND A LIST OF POSSIBLE PARENTS TO THE TEMPLATE
    # FORCING A PARENT SELECTION WHEN ADDING A SIBLING WILL ALLOW
    # MORE ACCURATE SEARCHING WHEN TRYING TO MATCH HALF OR
    # FULL SIBLINGS AND I WANT TO DO THIS WHERE POSSIBLE
    persons_parents = get_parents(person)
    mothers_partners_list = get_mothers_partners(person, persons_parents)
    fathers_partners_list = get_fathers_partners(person, persons_parents)

    # GET EXISTING SIBLINGS TO RETURN TO TEMPLATE FOR DISPLAYING
    existing_siblings = get_persons_data(person, 'siblings')
 
    # BUILD A LIST OF SIBLINGS, WITH PARENTS FOR COMPARISON
    # LATER IN POST SECTION
    sibling_and_parent_list = build_target_list(person, 'siblings')

    # WHEN FORM IS SUBMITTED / UPDATED
    if request.method == "POST":
        # GET THE TEMPLTE FROM THE FORM FOR SIBLING
        sibling_search = call_search()

        # GET THE 2 SELECTED PARENTS FROM THE FORM
        # EXTRACT THE 2 ID'S FROM THE RETURNED STRING
        selected_parents = choose_sibling_parents(persons_parents)

        # SEE IF PERSON ENTERED ON FORM EXISTS
        if mongo.db.people.count_documents(sibling_search, limit=1) == 0:
            # IF THEY DONT EXIST:
            # GET A SIBLING OBJECT TO CREATE THIS PERSON
            sibling = call_create_person(person, selected_parents)

            # INSERT THE NEW SIBLING THEN GET ID:
            mongo.db.people.insert_one(sibling)
            new_sibling_id = mongo.db.people.find_one(sibling)["_id"]

            # UPDATE THE PARENTS OF THIS NEW SIBLING AS THEIR NEW CHILD:
            # FIRST CHECK IN CASE ANY SELECTED PARENT IS BLANK - THIS
            # SHOULD NOT BE POSSIBLE.
            if any(value != "" for value in selected_parents.values()):
                for key, value in selected_parents.items():
                    mongo.db.people.find_one_and_update(
                        {"_id": ObjectId(value)}, {"$addToSet": {
                            "children": new_sibling_id}})

            # UPDATE PERSONS SIBLING ARRAY WITH ID FROM NEW SIBLING:
            mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(person_id)},
                    {"$addToSet": {"siblings": new_sibling_id}})

            # UPDATE NEW SIBLING WITH THE ID OF EACH EXISTING SIBLING OF PERSON
            for sibling_element in sibling_and_parent_list:
                mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(new_sibling_id)}, {"$addToSet": {
                        "siblings": sibling_element[0]}})

            # UPDATE EACH EXISTING SIBLING OF PERSON WITH THE ID FROM
            # NEW SIBLING
            for sibling_element in sibling_and_parent_list:
                mongo.db.people.find_one_and_update(
                    {"_id": sibling_element[0]}, {"$addToSet": {
                        "siblings": new_sibling_id}})

        else:
            #   ELSE THE SIBLING DOES EXIST IN DB, SO WE FIND AND UPDATE THEM:

            #   GET THE FOUND SIBLING
            found_sibling = mongo.db.people.find_one(sibling_search)
            found_sibling_id = found_sibling["_id"]

            #   WE REMOVE THE FOUND SIBLING ID FROM ANY CHILDREN
            #       ARRAY - THIS IS BECAUSE WE ARE POSTING NEW PARENTS.
            #   FOR EXAMPLE: WE DONT WANT SIBLING HAVING 2 BIRTH MOTHERS.
            mongo.db.people.update({}, {"$pull": {
             "children": {"$in": [found_sibling_id]}}}, multi=True)

            #   WE REMOVE THE FOUND SIBLING ID FROM ANY SIBLING
            #       ARRAY - THIS IS IN CASE THE PARENTS ARE CHANGING
            #   SIBLINGS WILL BE REASSIGNED, IF AT LEAST ON PARENT MATCHES
            mongo.db.people.update({}, {"$pull": {
             "sibling": {"$in": [found_sibling_id]}}}, multi=True)

            # UPDATE THE FOUND SIBLING WITH USER SELECTED PARENTS.
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(found_sibling_id)},
                {"$set": {"parents": selected_parents}})

            # ADD FOUND SIBLING TO THE PARENTS CHILDREN ARRAY
            if any(x != "" for x in selected_parents.values()):
                for key, value in selected_parents.items():
                    mongo.db.people.find_one_and_update(
                        {"_id": ObjectId(value)}, {"$addToSet": {
                            "children": found_sibling_id}})

            # GET ANY EXISTING SIBLINGS OF FOUND SIBLING
            # ADD FOUND SIBLING WITH THEIR SIBLINGS TO A NEW LIST:
            found_siblings_of_sibling = found_sibling["siblings"]
            found_siblings_of_sibling.insert(0, found_sibling_id)

            # GET EACH OF THESE FOUND SIBLINGS INTO A COMBINED
            # LIST WITH PARENTS SO WE CAN COMPARE THEM
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


# CHECK PARTNER EXISTS VIEW
@app.route("/check_if_partner_exists/<person_id>")
def check_if_partner_exists(person_id):

    # FUNCTION THAT CHECKS IF PERSON BEING EDITED HAS ANY PARTNERS
    # IF YES- CONTINUE TO ASSIGN CHILDREN
    # IF NO - GIVE OPTION SCREEN WHAT TO DO NEXT

    # SETUP VARIABLES
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    persons_spouse_partner_ids = person["spouse_partner"]

    # RUN THE CHECK
    if len(persons_spouse_partner_ids) > 0:
        return redirect(url_for(
            "assign_children", person_id=person_id))

    return render_template("check_if_partner_exists.html", person=person)


# ASSIGN CHILDREN VIEW
@app.route("/assign_children/<person_id>", methods=["GET", "POST"])
def assign_children(person_id):

    # FUNCTION PURPOSE -
    # 1.    GETS THE PERSONS CHILDREN INFORMATION AND DISPLATS IT WITHIN
    #       THE TEMPLATE.
    # 2.    DISPLAYS CURRENT CHILDREN.
    # 3.    GETS THE CHILDREN INFO AND GETS IT READY TO BE COMPARED WHEN
    #       POSTING
    #       THIS WAS TO SOLVE A SCALING ISSUE WHERE WHEN I TRIED TO ADD 10
    #       CHILDREN THE SYSTEM TIMED OUT, IT WAS DOING TO MUCH IN THE
    #       POST SECTION, AS IT HAD TO CHECK EVERY SIBLING AND CHECK IF AT
    #       LEAST ONE PARENT MATCHED.
    # AFTER POST -
    # 1.    SEARCH FOR THE CHILD ENTERED FROM THE FORM GRAB PARENTS FROM
    #       THE FORM
    # 2.    IF CHILD DOES NOT EXIST - CREATE IT, LINK ITS SIBLINGS,
    #       UPDATE OTHER SIBLINGS, PARENTS AND INSERT INTO PARENTS AS A CHILD
    # 3.    ELSE IF THE CHILD DOES EXIST:
    #       - CHECK FOR MATCHING PARENTS.
    #       - LINK IT TO ITS NEW SIBLINGS.
    #       - UPDATE ITS NEW & OLD SIBLINGS.
    #       - UPDATE PARENTS AND UPDATE NEW AND OLD PARENTS CHILDREN

    # SETUP SOME REQUIRED VARIABLES
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    persons_id = person["_id"]

    # GET EXISTING SIBLINGS TO RETURN TO TEMPLATE FOR DISPLAYING
    existing_children = get_persons_data(person, 'children')

    # PERSONS SPOUSE_PARTNER - CHECK IF SPOUSE/PARTNERS ALREADY LINKED
    persons_spouse_partners = get_persons_data(person, 'spouse_partner')

    # BUILD A LIST OF CHILDREN, WITH PARENTS FOR COMPARISON
    # LATER IN POST SECTION
    children_and_parent_list = build_target_list(person, 'children')

    if request.method == "POST":
        # GET THE TEMPLTE FROM THE FORM FOR CHILD
        child_search = call_search()

        # GET THE SELECTED PARENTS
        child_parents = get_selected_parents(person, persons_spouse_partners)

        # GET THE OBJECT OF THE OTHER PARENT CHOSEN WITH PERSON.
        selected_parent = get_chosen_parent(persons_spouse_partners)

        # GET THE OTHER PARENTS CHILDREN
        selected_parent_children = build_target_list(
            selected_parent, 'children')

        # UPDATE children_and_parent_list LIST
        for group in selected_parent_children:
            if group not in children_and_parent_list:
                children_and_parent_list.append(group)

        # SEE IF THE CHILD ENTERED ON FORM EXISTS
        if mongo.db.people.count_documents(child_search, limit=1) == 0:

            # IF THEY DONT EXIST:
            # 1.    CREATE THE CHILD
            # 2.    UPDATE PARENTS WITH THIS NEW CHILD
            # 3.    UPDATE ALL CHILDREN OF PARENTS INCLUDING THIS NEW
            #       CHILD WITH THEIR NEW SIBLINGS

            # GET A CHILD OBJECT TEMPLATE TO CREATE THIS PERSON
            child = call_create_person(person, child_parents)

            #   INSERT THE NEW CHILD THEN GET ID
            mongo.db.people.insert_one(child)
            child_id = mongo.db.people.find_one(child)["_id"]

            # UPDATE THE PARENTS
            if any(value != "" for value in child_parents.values()):
                for key, value in child_parents.items():
                    mongo.db.people.find_one_and_update(
                        {"_id": ObjectId(value)}, {"$addToSet": {
                            "children": child_id}})

            # UPDATE NEW CHILD WITH THE ID OF EACH EXISTING CHILD OF PARENTS -
            # WHICH WILL ALL BE SIBLINGS OF NEW CHILD
            for child_element in children_and_parent_list:
                mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(child_id)}, {"$addToSet": {
                        "siblings": child_element[0]}})

            # UPDATE ALL THE NEW SIBLINGS WITH THIS NEW CHILD AS A SIBLING
            for child_element in children_and_parent_list:
                mongo.db.people.find_one_and_update(
                    {"_id": child_element[0]}, {"$addToSet": {
                        "siblings": ObjectId(child_id)}})

        else:

            # IF THEY DO EXIST:
            # 1.    FIND THE CHILD
            # 2.    DELETE FOUND CHILD FROM ANY SIBLINGS ARRAY IN DB
            # 3.    DELETE FOUND CHILD FROM ANY CHILDREN ARRAY IN DB
            #       (STEPS 2 AND 3 ARE IN CASE OF CHANGE OF PARENTS)
            # 4.    ASSIGN SELECTED PARENTS TO FOUND CHILD
            # 5.    ASSIGN FOUND CHILD TO SELECTED PARENTS AS A CHILD
            # 6.    GET ALL POSSIBLE SIBLINGS AND CHECK IF EACH HAS
            #       AT LEAST ONE MATCHING PARENT. IF THEY DO THEY CAN BE
            #       LINKED AS SIBLINGS

            # FIND THE CHILD
            found_child = mongo.db.people.find_one(child_search)
            child_id = found_child["_id"]

            #   DELETE FOUND CHILD FROM ANY SIBLINGS ARRAY IN DB
            mongo.db.people.update({}, {"$pull": {
                "siblings": {"$in": [child_id]}}}, multi=True)

            #   DELETE FOUND CHILD FROM ANY CHILDREN ARRAY IN DB
            mongo.db.people.update({}, {"$pull": {
                "children": {"$in": [child_id]}}}, multi=True)

            # ASSIGN SELECTED PARENTS TO FOUND CHILD
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(child_id)},
                {"$set": {"parents": child_parents}})

            # UPDATE THE PERSON WITH THEIR CHILD
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(persons_id)},
                {"$addToSet": {"children": child_id}})

            # UPDATE THE PERSONS SPOUSE / PARTNER WITH THEIR CHILD
            if selected_parent['_id']:
                mongo.db.people.find_one_and_update(
                    {"_id": selected_parent['_id']},
                    {"$addToSet": {"children": child_id}})

            # UPDATE children_and_parent_list WITH THIS CHILD AND PARENTS

            # GET ANY EXISTING SIBLINGS OF FOUND CHILD
            # ADD FOUND CHILD WITH THEIR SIBLINGS TO A NEW LIST:
            found_siblings_of_child = found_child["siblings"]
            found_siblings_of_child.insert(0, child_id)

            # GET EACH OF THESE FOUND SIBLINGS INTO A COMBINED
            # LIST WITH PARENTS SO WE CAN COMPARE THEM
            full_sibling_parent_list = merge_target_parent_list(
                found_siblings_of_child, children_and_parent_list)

            link_real_siblings(full_sibling_parent_list)

        flash("Circle has been updated")
        return redirect(url_for("assign_children", person_id=person_id))

    return render_template(
        'assign_children.html',
        persons_spouse_partners=persons_spouse_partners,
        existing_children=existing_children, person=person)


#   MANAGE A SPOUSE OR PARTNER RELATIONSHIP VIEW
@app.route(
    "/manage_partner_relationship/<person_id>/<person2_id>")
def manage_partner_relationship(person_id, person2_id):

    # FUNCTION PURPOSE -
    # 1.    A BUFFER/CONFIRMATION HANDLER FOR THE UNLINKING
    #       OF A PERSON FROM A SPOUSE/PARTNER
    # 2.    THIS FUNCTION DECIDES IF THE USER SHOULD BE ABLE
    #       TO UNLINK A SPOUSE OR PARTNER.
    # 3.    UNLINK=TRUE OR FALSE IS THE KEY, TO ALLOWING
    #       JINGA TO SHOW CORRECT OPTION

    # SETUP VARIABLES
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    person2 = mongo.db.people.find_one({"_id": ObjectId(person2_id)})
    partner_children = person2['children']
    person_children = person['children']
    unlink = False
    message = ""

    #   CHECK IF PERSON HAS ANY CHILDREN - IF HE DOES
    #   CHECK DO THEY MATCH ANY OF THE PARTNERS CHILDREN
    #   IF THEY DO, WE MUST NOT UNLINK

    #   DOES PERSON BEING EDITED HAVE ANY CHILDREN
    if len(person_children) > 0:
        #   IF YES, THEN CHECK IF ANY MATCH THE PARTNERS CHILDREN
        check = any(
            item in person_children for item in partner_children)

        #   IF THERE IS A MATCH - THEN DO NOT ALLOW UNLINKING
        if check is True:
            unlink = False
        else:
            unlink = True
    #   ELSE WE CAN ALLOW UNLINKING
    else:
        unlink = True

    return render_template(
        "manage_partner_relationship.html", unlink=unlink, person2=person2,
        person=person, message=message)


#   REMOVE A SPOUSE OR PARTNER AS A SPOUSE OR PARTNER VIEW
@app.route(
    "/delete_partner_relationship/<person_id>/<person2_id>",
    methods=["GET", "POST"])
def delete_partner_relationship(person_id, person2_id):

    # FUNCTION PURPOSE -
    # 1.    PERFORMS THE UNLINKING OF A
    #       PERSON AND A SPOUSE_PARTNER

    #   SETUP VARIABLES
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    person2 = mongo.db.people.find_one({"_id": ObjectId(person2_id)})
    partners_id = person2['_id']
    persons_id = person['_id']

    #   PERFORM THE UNLINKING
    mongo.db.people.update({"_id": ObjectId(partners_id)}, {
        "$pull": {"spouse_partner": {"$in": [persons_id]}}})
    mongo.db.people.update({"_id": ObjectId(persons_id)}, {
        "$pull": {"spouse_partner": {"$in": [partners_id]}}})

    #   RETURN PERSON_ID TO THE ASSIGN SPOUSE ROUTE
    flash("Spouse / Partner relationship has been removed")
    return redirect(url_for(
            "assign_spouse_partner", person_id=person_id))

    # return render_template("assign_spouse_partner.html", person_id=person_id)


#   MANAGE A SIBLING RELATIONSHIP VIEW
@app.route(
    "/manage_sibling_relationship/<person_id>/<person2_id>")
def manage_sibling_relationship(person_id, person2_id):

    # FUNCTION PURPOSE -
    # 1.    A BUFFER/CONFIRMATION HANDLER FOR THE UNLINKING
    #       OF A PERSON FROM A SIBLING
    # 2.    THIS FUNCTION SIMPLY REMINDS THE USER OF WHAT THEY
    #       ARE DOING, AND GIVES THEM A CHOICE OF ACTIONS

    #   SETUP SOME REQ VARIABLES
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    person2 = mongo.db.people.find_one({"_id": ObjectId(person2_id)})

    return render_template(
        "manage_sibling_relationship.html", person2=person2,
        person=person)


# REMOVE SIBLING RELATIONSHIP VIEW
@app.route(
    "/delete_sibling_relationship/<person_id>/<person2_id>",
    methods=["GET", "POST"])
def delete_sibling_relationship(person_id, person2_id):

    # FUNCTION PURPOSE -
    # 1.    PERFORMS THE UNLINKING OF A
    #       PERSON AND A SIBLING

    # SETUP VARIABLES
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})['_id']
    sibling = mongo.db.people.find_one({"_id": ObjectId(person2_id)})['_id']

    # REMOVE SIBLING LINKS
    mongo.db.people.update({"_id": ObjectId(person)}, {
        "$pull": {"siblings": {"$in": [sibling]}}})
    mongo.db.people.update({"_id": ObjectId(sibling)}, {
        "$pull": {"siblings": {"$in": [person]}}})

    # RETURN PERSON_ID TO THE ASSIGN SIBLING ROUTE
    flash("Sibling relationship has been removed")
    return redirect(url_for(
            "assign_siblings", person_id=person_id))

    # return render_template("assign_spouse_partner.html", person_id=person_id)


#  MANAGE A CHILD RELATIONSHIP VIEW
@app.route("/manage_child_relationship/<person_id>/<person2_id>")
def manage_child_relationship(person_id, person2_id):

    # FUNCTION PURPOSE -
    # 1.    A BUFFER/CONFIRMATION HANDLER FOR THE UNLINKING
    #           OF A PERSON FROM A CHILD
    # 2.    THIS FUNCTION SIMPLY REMINDS THE USER OF WHAT THEY
    #           ARE DOING, AND GIVES THEM A CHOICE OF ACTIONS

    #   SETUP SOME REQ VARIABLES
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    person2 = mongo.db.people.find_one({"_id": ObjectId(person2_id)})

    return render_template(
        "manage_child_relationship.html", person2=person2,
        person=person)


# HANDLE REMOVING A CHILD VIEW
@app.route(
    "/delete_child_relationship/<person_id>/<person2_id>",
    methods=["GET", "POST"])
def delete_child_relationship(person_id, person2_id):

    # FUNCTION  - PERFORMS THE UNLINKING OF A
    #           - PERSON AND A CHILD

    # SETUP VARIABLES
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    person_id = person['_id']
    child = mongo.db.people.find_one({"_id": ObjectId(person2_id)})
    child_id = child['_id']
    child_parents = child['parents']

    #   DECIDE GENDER OF PERSON - SO WE KNOW IF WE ARE REMOVING A MOTHER
    #   OR A FATHER
    removed_parent_gender = person['gender']
    if removed_parent_gender == 'male':
        child_parents['father'] = ""
    else:
        child_parents['mother'] = ""

    # REMOVE CHILDREN LINKS
    mongo.db.people.update({"_id": ObjectId(person_id)}, {
        "$pull": {"children": {"$in": [child_id]}}})
    mongo.db.people.find_one_and_update(
                {"_id": ObjectId(child_id)},
                {"$set": {"parents": child_parents}})

    # RETURN PERSON_ID TO THE ASSIGN CHILDREN ROUTE
    flash("Children relationship has been removed")
    return redirect(url_for(
            "assign_children", person_id=person_id))

    return render_template("assign_spouse_partner.html", person_id=person_id)


#   EDIT PERSON VIEW
@app.route("/edit_person/<person_id>", methods=["GET", "POST"])
def edit_person(person_id):

    # FUNCTION PURPOSE -
    # 1.    GETS INFORMATION FROM THE PERSON BEING EDITED AND DISPLAYS
    #       IT IN A FORM.
    # 2.    ALLOW THE USER TO EDIT THIS FORM AND UPDATE THE PERSON IN THE DB
    # 3     THE USER ENTERED DATA WILL BE ASSIGNED TO THE ORIGINAL PERSON ID
    #       UNLESS THERE IS A MATCHING FIRST NAME, LAST NAME AND DOB IN THE DB.
    #       IN THIS CASE THE USER WILL BE NOTIFIED, THE POST CANCELLED,
    #       AND THE USER WILL BE RETURNED TO THE ORIGINAL EDIT FORM.

    # GETTING INFORMATION
    # SETUP REQ VARIABLES
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    families = mongo.db.family.find().sort("family_name", 1)

    if request.method == "POST":
        #   SEARCH FOR EXISTING PERSON - AVOIDING DUPLICATION
        person_search = call_search()

        #   BUILD AN UPDATE FOR AN EXISTING PERSON
        person_update = call_person_update()

        #    CHECK TO SEE IF PERSON ALREADY EXISTS
        if mongo.db.people.count_documents(person_search, limit=1) == 0:
            #   ADD THE PERSON DICTIONARY TO MONGO
            #   INSERT NEW PERSON
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(person_id)},
                {"$set": person_update})

            flash("Circle has been updated")
            return redirect(url_for(
                "assign_parents", person_id=person_id))
        else:
            #   THEN PERSON ALREADY EXISTS, GET THE DUPLICATE
            #   THEN WE INFORM USER
            duplicate_id = mongo.db.people.find_one(
                person_search)['_id']
            person_id = mongo.db.people.find_one(
                {"_id": ObjectId(person_id)})['_id']

            # IF THE DUPLICATE FOUND IS THE PERSON BEING EDITED
            if duplicate_id == person_id:
                # UPDATE ANYWAY
                mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(person_id)},
                    {"$set": person_update})

                flash("Circle has been updated")
                return redirect(url_for(
                    "assign_parents", person_id=person_id))

            # NOTIFY USER OF ENTRY CONFLICT WITH ANOTHER PERSON
            return redirect(url_for("notify_duplicate", person_id=person_id,
                                    duplicate_id=duplicate_id))

    # RETURN THE FAMILIES TO THE ADD_PERSON PAGE FOR JINGA
    return render_template(
        "edit_person.html", person=person, families=families)


# NOTIFY IF DUPLICATE PERSON VIEW
@app.route("/notify_duplicate/<person_id>/<duplicate_id>")
def notify_duplicate(person_id, duplicate_id):

    # FUNCTION PURPOSE -
    # 1.       TO NOTIFY USER OF DUPLICATION AND PROVIDE OPTIONS

    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    duplicate = mongo.db.people.find_one({"_id": ObjectId(duplicate_id)})

    return render_template(
        "notify_duplicate.html", person=person, duplicate=duplicate)


# VIEW CIRCLE VIEW
@app.route("/view_circle/<person_id>")
def view_circle(person_id):

    # FUNCTION PURPOSE -
    # 1.    TO DISPLAY A CHOSEN FAMILY CIRCLE

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

    #   GET PARENTS
    if persons_mother != "":
        #   THEN IT HAS EXISTING MOTHER - SO ASSIGN THE ID
        mother = mongo.db.people.find_one({
            "_id": ObjectId(persons_mother)
            })
    if persons_father != "":
        #   THEN IT HAS EXISTING FATHER - SO ASSIGN THE ID
        father = mongo.db.people.find_one({
            "_id": ObjectId(persons_father)
            })

    #   GET SPOUSE/PARTNERS
    for partner in spouse_partner:
        spouse_partner_list.append(mongo.db.people.find_one({
            "_id": ObjectId(partner)
            }))

    #   GET SIBLINGS
    for sibling in siblings:
        siblings_list.append(mongo.db.people.find_one({
            "_id": ObjectId(sibling)
            }))

    #   GET CHILDREN
    for child in children:
        children_list.append(mongo.db.people.find_one({
            "_id": ObjectId(child)
            }))

    return render_template(
        "view_circle.html", person=person, mother=mother, father=father,
        spouse_partner_list=spouse_partner_list, siblings_list=siblings_list,
        children_list=children_list)


# MANAGE PEOPLE ROUTE
@app.route("/manage_people", methods=["GET", "POST"])
def manage_people():

    # FUNCTION PURPOSE -
    # 1.    DISPLAY THE MANAGE PEOPLE PAGE
    # 2.    ENABLE SEARCH AND FIND PERSON TO DELETE
    # 3.    GIVES THE RESULTS WITH OPTION TO REMOVE PERSON

    people = {}
    error = ""
    if request.method == "POST":
        #   BUILD A SEARCH OBJECT
        query = call_search()

        #   CHECK IF THE QUERY IS NOT BLANK - SOMEONE JUST CLICKED
        #       SEARCH WITHOUT ANY ENTRIES?
        if len(query) > 0:
            people = list(mongo.db.people.find(query))
            error = "Sorry we have no records matching your query."
        else:
            return redirect(url_for("manage_people"))

    return render_template("manage_people.html", people=people, error=error)


# DELETE PERSON ROUTE
@app.route("/delete_person/<person_id>", methods=["GET", "POST"])
def delete_person(person_id):

    # FUNCTION PURPOSE -
    # 1.    DELETES THE DOCUMENT FOR THE USER ID PASSED IN
    # 2.    DELETES ANY FOREIGN KEYS
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    persons_id = person["_id"]

    # REMOVE ALL INSTANCES WHERE THIS PERSONS ID IS A FOREIGN
    # ID IN ANOTHER DOCUMENTS ARRAY
    remove_all_links(persons_id)

    # REMOVE ANY LINKS TO PARENTS AS THIS IS AN OBJECT
    remove_parent_link(person)

    flash("Person has been successfully removed from Circles")

    return render_template("manage_people.html")


@app.route("/delete_all_documents", methods=["GET", "POST"])
def delete_all_documents():

    # FUNCTION PURPOSE -
    # 1.    CHECKS IF CORRECT DELETION PASSWORD HAS BEEN ENTERED
    # 2.    DELETES ALL PEOPLE FROM DB

    if check_password_hash(
                mongo.db.users.find_one(
                    {'user_name': 'validation'})["del_password"],
                request.form.get("password")):
        # mongo.db.people.remove({})
        flash("Circles has been Deleted")
        return redirect(url_for("manage_people"))
    else:
        flash("The password you entered was incorrect.\
            Circles has not been Deleted.")

    return render_template("manage_people.html")


@app.route("/change_password", methods=["GET", "POST"])
def change_password():

    # FUNCTION PURPOSE -
    # 1.    TO CHANGE THE DELETION PASSWORD

    if request.method == "POST":
        if check_password_hash(
            mongo.db.users.find_one(
                {'user_name': 'validation'})["del_password"], request.form.get(
                    "existing_password")):
            # DO ADDITIONAL CHECK TO CONFIRM NEW PASSWORDS MATCH
            password1 = request.form.get("new_password")
            password2 = request.form.get("repeat_new_password")
            if password1 == password2:
                new_password = {
                    'del_password': generate_password_hash(
                        request.form.get("new_password"))
                }
                # UPDATE THE NEW PASSWORD
                mongo.db.users.find_one_and_update(
                    {"user_name": "validation"}, {"$set": new_password})

                flash("The password has been updated")

        else:
            flash("The password you entered did not match.\
                The Password has not been changed")

    return render_template("manage_people.html")

# ROUTE TO HANDLE E404
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


# ROUTE TO HANDLE E500
@app.errorhandler(500)
def server_error(e):
    return render_template("500.html")


# TELL OUR APP, HOW AND WHERE TO RUN OUR APPLICATION
if __name__ == "__main__":
    # SET THE HOST TO THE DEFAULT IP FOUND IN ENV.PY
    app.run(host=os.environ.get("IP"),
            # CONVERT THE PORT TO AN INT
            port=int(os.environ.get("PORT")),
            # SET DEBUG TO FALSE WHEN FINISHED DEVELOPING
            debug=True)



###################################################################

## remove debug
## remove coment out on delete all circles


###################################################################
###################################################################
###################################################################