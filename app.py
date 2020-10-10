import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from pymongo import ReturnDocument 

from bson.objectid import ObjectId
from werkzeug.security import (
    generate_password_hash, check_password_hash)

# Import env.py if it exists
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

# SETUP OUR env VARIABLES
# MONGO DBNAME
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
# GET THE MONGO URI OR CONNECTION STRING
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# GET THE SECRET KEY WHICH IS REQUIRED FOR PARTS OF FLASK, LIKE FLASH
app.secret_key = os.environ.get("MONGO_DBNAME")

# SETUP INSTANCE OF PyMongo AND ADD IN app.py
mongo = PyMongo(app)


# BASE ROUTE
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

# SEARCH
@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        # SETUP A DICTIONARY THAT HOLDS THE INFOR WE CAN QUERY
        # IT WILL POPULATE FROM THE FORM.
        searchInput = {
            "first_name": request.form.get("searchFirstName").lower(),
            "last_name": request.form.get("searchLastName").lower(),
            "dob": request.form.get("searchDob"),
            }
        # SETUP A BLANK QUERY DICTIONARY AND THEN LOOP OVER
        # searchInput ABOVE TO BUILD A QUERY FROM ONLY POPULATED
        # VALUES
        query = {}
        for k, v in searchInput.items():
            if len(v) > 0:
                query[k] = v

        # CHECK IF THE QUERY IS NOT  BLANK - SOMEONE JUST CLICKED
        # SEARCH WITHOUT ANY ENTRIES
        if len(query) > 0:
            people = list(mongo.db.people.find(query))
            error = "Sorry we have no records matching your query."
        else:
            return redirect(url_for("home"))

        # RETURN TO HOME, THE RESULTS CURSOR
    return render_template("home.html", people=people, error=error)


# ADD PERSON ROUTE
@app.route("/add_person/", methods=["GET", "POST"])
def add_person():

    if request.method == "POST":
        # USED TO SEARCH FOR EXISTING PERSON
        person_search = {
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "gender": request.form.get("gender"),
            "dob": request.form.get("dob"),
        }
        # USED TO UPDATE AN EXISTING PERSON
        person_update = {
            "family_name": request.form.get("family_name").lower(),
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "birth_surname": request.form.get("birth_surname"),
            "gender": request.form.get("gender"),
            "dob": request.form.get("dob"),
            "dod": request.form.get("dod"),
            "birth_address": request.form.get("birth_address"),
            "rel_address": request.form.get("rel_address"),
            "information": request.form.get("person_info"),
        }

        # CHECK TO SEE IF PERSON ALREADY EXISTS
        if mongo.db.people.count_documents(person_search, limit=1) == 0:
            # SETUP DICTIONARY FOR IMPORTING PERSON TO MONGO DB
            person = {
                "family_name": request.form.get("family_name").lower(),
                "first_name": request.form.get("first_name").lower(),
                "last_name": request.form.get("last_name").lower(),
                "birth_surname": request.form.get("birth_surname"),
                "parents": {"mother": "", "father": ""},
                "siblings": [],
                "spouse_partner": [],
                "gender": request.form.get("gender"),
                "dob": request.form.get("dob"),
                "dod": request.form.get("dod"),
                "birth_address": request.form.get("birth_address"),
                "rel_address": request.form.get("rel_address"),
                "information": request.form.get("person_info"),
                "children": []
            }
            # ADD THE PERSON DICTIONARY TO MONGO
            person_inserted = mongo.db.people.insert_one(person)
            person_id = person_inserted.inserted_id
        else:
            # THEN PERSON ALREADY EXISTS, WE CAN UPDATE THEM
            person_id = mongo.db.people.find_one(
                person_search)["_id"]
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(person_id)},
                {"$set": person_update})

        flash("This Person has bees successfully added to Circles")
        return redirect(url_for(
            "edit_parents", person_id=person_id))

    # GET THE FAMILY COLLECTION NAMES, FOR THE FAMILY
    # SELECTION DROP DOWN
    families = mongo.db.family.find().sort("family_name", 1)
    # RETURN THE FAMILIES TO THE ADD_PERSON PAGE FOR JINGA
    return render_template(
        "add_person.html", families=families)


# EDIT PARENTS ROUTE AND FUNCTION
@app.route("/edit_parents/<person_id>", methods=["GET", "POST"])
def edit_parents(person_id):

    # SETUP SOME REQUIRED VARIABLES
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    persons_id = person["_id"]
    persons_mother_id = person["parents"]["mother"]
    persons_father_id = person["parents"]["father"]

    # PERSONS MOTHER - CHECK IF MOTHER ALREADY LINKED
    if persons_mother_id != "":
        # THEN IT HAS EXISTING MOTHER - SO ASSIGN THE ID
        existing_mother = mongo.db.people.find_one({
            "_id": ObjectId(persons_mother_id)
            })
    else:
        # ITS A NEW MOTHER - NO TEMPLATE YET
        # SO WE GIVE IT ONE
        existing_mother = {
            "first_name": "",
            "last_name": "",
            "dob": ""
        }

    # PERSONS FATHER - CHECK IF FATHER ALREADY LINKED
    if persons_father_id != "":
        # THEN IT HAS EXISTING FATHER - SO ASSIGN THE ID
        existing_father = mongo.db.people.find_one({
            "_id": ObjectId(persons_father_id)
            })
    else:
        # ITS A NEW FATHER - NO TEMPLATE YET
        # SO WE GIVE IT ONE
        existing_father = {
            "first_name": "",
            "last_name": "",
            "dob": ""
        }

    # WHEN FORM IS SUBMITTED / UPDATED
    if request.method == "POST":

        # IMPORTANT - WE REMOVE THE PERSONS ID FROM ANY CHILDREN
        # ARRAY - THIS IS BECAUSE WE ARE POSTING NEW PARENTS.
        # FOR EXAMPLE: WE DONT WANT PERSON HAVING 2 BIRTH MOTHERS.
        mongo.db.people.update({}, {"$pull": {
             "children": {"$in": [persons_id]}}}, multi=True)

        # GET THE TEMPLTE FROM THE FORM
        # FOR MOTHER
        mother = {
            "first_name": request.form.get("mothers_first_name").lower(),
            "last_name": request.form.get("mothers_last_name").lower(),
            "dob": request.form.get("mothers_dob")
        }
        # FOR FATHER
        father = {
            "first_name": request.form.get("fathers_first_name").lower(),
            "last_name": request.form.get("fathers_last_name").lower(),
            "dob": request.form.get("fathers_dob")
        }

        # FIRST WE CHECK IF MOTHER EXISTS ANYWHERE IN THE DB
        if mongo.db.people.count_documents(mother, limit=1) == 0:
            # IF THE COUNT IS == O, THEN WE INSERT A NEW MOTHER
            mother = {
                "family_name": person["family_name"].lower(),
                "first_name": request.form.get(
                    "mothers_first_name").lower(),
                "last_name": request.form.get("mothers_last_name").lower(),
                "birth_surname": "",
                "parents": {"mother": "", "father": ""},
                "siblings": [],
                "spouse_partner": [],
                "gender": "Female",
                "dob": request.form.get("mothers_dob"),
                "dod": "",
                "birth_address": "",
                "rel_address": "",
                "information": "",
                "children": [persons_id]
            }
            # INSERT THE NEW MOTHER, THEN GET BACK THE ID
            mongo.db.people.insert_one(mother)
            mother_id = mongo.db.people.find_one(mother)["_id"]

        else:
            # IF THE COUNT IS NOT == O, THEN WE HAVE A MATCH FOR MOTHER
            # SO WE UPDATE THAT MOTHER WITH THEIR NEW CHILD
            found_mother = mongo.db.people.find_one(mother)["_id"]
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(found_mother)},
                {"$addToSet": {"children": persons_id}})
            mother_id = found_mother

        # NEXT WE CHECK IF FATHER EXISTS ANYWHERE IN THE DB
        if mongo.db.people.count_documents(father, limit=1) == 0:
            # IF THE COUNT IS == O, THEN WE INSERT A NEW FATHER
            father = {
                "family_name": person["family_name"].lower(),
                "first_name": request.form.get(
                    "fathers_first_name").lower(),
                "last_name": request.form.get(
                    "fathers_last_name").lower(),
                "birth_surname": "",
                "parents": {"mother": "", "father": ""},
                "siblings": [],
                "spouse_partner": [],
                "gender": "Male",
                "dob": request.form.get("fathers_dob"),
                "dod": "",
                "birth_address": "",
                "rel_address": "",
                "information": "",
                "children": [persons_id]
            }
            # INSERT THE NEW FATHER, THEN GET BACK THE ID
            mongo.db.people.insert_one(father)
            father_id = mongo.db.people.find_one(father)["_id"]

        else:
            # IF THE COUNT IS NOT == O, THEN WE HAVE A MATCH FOR FATHER
            # WE ADD PERSON AS A CHILD
            # WE UPDATE THAT FATHER
            found_father = mongo.db.people.find_one(father)["_id"]
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(found_father)},
                {"$addToSet": {"children": persons_id},
                 "$set": father})
            father_id = found_father

        # HERE WE BUILD THE PARENTS INTO A DICT AND SET IT INSIDE THE PERSON
        parents = {"mother": mother_id, "father": father_id}
        mongo.db.people.find_one_and_update(
            {"_id": ObjectId(person_id)}, {"$set": {"parents": parents}})

        # WE ALSO NEED TO ADD THE PARENTS AS A SPOUSE / PARTNERS OF
        # EACH OTHER, BECAUSE THEY HAVE A SIGNIFICANT RELATIONSHIP
        # DUE TO HAVING A CHILD TOGETHER
        mongo.db.people.find_one_and_update(
            {"_id": ObjectId(mother_id)},
            {"$addToSet": {"spouse_partner": father_id}})
        mongo.db.people.find_one_and_update(
            {"_id": ObjectId(father_id)},
            {"$addToSet": {"spouse_partner": mother_id}})

        #   GET THE CHILDREN OF BOTH PARENTS AND ADD THEM AS SIBLINGS OF
        #   THE PERSON BEING EDITED
        mothers_children = mongo.db.people.find_one(
            {"_id": ObjectId(mother_id)})["children"]
        fathers_children = mongo.db.people.find_one(
            {"_id": ObjectId(father_id)})["children"]
        combined_children = list(set(mothers_children + fathers_children))
        for child in combined_children:
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(person_id)},
                {"$addToSet": {"siblings": child}})


         # COMBINE THESE LISTS OF SIBLINGS
          #  person_and_sibling_list = [persons_id, found_sibling_id]
           # combined_siblings = list(set(
            #    person_and_sibling_list + sibling_siblings_id_list))

        flash("Circle has been updated")
        return redirect(url_for("edit_spouse_partner", person_id=person_id))

    return render_template(
        "edit_parents.html", existing_mother=existing_mother,
        existing_father=existing_father, person=person)


# ROUTE TO HANDLE ADDING A SPOUSE/PARTNER
@app.route("/edit_spouse_partner/<person_id>", methods=["GET", "POST"])
def edit_spouse_partner(person_id):

    # SETUP SOME REQUIRED VARIABLES
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    persons_id = person["_id"]
    persons_spouse_partner_ids = person["spouse_partner"]
    existing_spouse_partners = {}

    # PERSONS SPOUSE_PARTNER - CHECK IF SPOUSE/PARTNERS ALREADY LINKED
    if len(persons_spouse_partner_ids) > 0:
        # THEN PERSON HAS EXISTING SPOUSE_PARTNERS - SO GET THEM INTO
        # A DICT, START INDEX AT ASCII 97 'a' WAS HAVING TROUBLE WITH
        # '0' AS A KEY
        for index, spouse_partner in enumerate(persons_spouse_partner_ids, 97):
            existing_spouse_partners[chr(index)] = mongo.db.people.find_one({
                "_id": ObjectId(spouse_partner)
                })
    else:
        # PASS AN EMPTY DICT INTO THE TEMPLATE
        existing_spouse_partners = {}

    if request.method == "POST":
        # GET THE TEMPLATE FROM THE FOR PARTNER/SPOUSE
        spouse_partner_search = {
            "first_name": request.form.get(
                "spouse_partner_first_name").lower(),
            "last_name": request.form.get("spouse_partner_last_name").lower(),
            "dob": request.form.get("spouse_partner_dob")
        }

        # SEE IF PERSON ENTERED ON FORM EXISTS
        if mongo.db.people.count_documents(
                spouse_partner_search, limit=1) == 0:

            # THIS IS THE CASE THAT THIS ENTERED SPOUSE/PARTNER DOES NOT EXIST
            # IN THE DB. IT IS TEMPLATE WE USE TO CREATE A NEW SPOUSE/PARTNER
            spouse_partner = {
                "family_name": person["family_name"].lower(),
                "first_name": request.form.get(
                    "spouse_partner_first_name").lower(),
                "last_name": request.form.get(
                    "spouse_partner_last_name").lower(),
                "birth_surname": "",
                "parents": {"mother": "", "father": ""},
                "siblings": [],
                "spouse_partner": [],
                "gender": request.form.get("gender"),
                "dob": request.form.get("spouse_partner_dob"),
                "dod": "",
                "birth_address": "",
                "rel_address": "",
                "information": "",
                "children": []
            }
            # INSERT THE NEW SPOUSE/PARTNER THEN GET ID IN CORRECT FORMAT
            mongo.db.people.insert_one(spouse_partner)
            new_spouse_partner_id = mongo.db.people.find_one(
                spouse_partner)["_id"]
            mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(new_spouse_partner_id)},
                    {"$addToSet": {"spouse_partner": persons_id}})

            # UPDATE PERSONS SPOUSE/PARTNER ARRAY WITH ID
            # FROM NEW SPOUSE/PARTNER
            mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(person_id)},
                    {"$addToSet": {"spouse_partner": new_spouse_partner_id}})

        else:
            # ELSE THE SPOUSE/PARTNER DOES EXIST IN DB, SO WE UPDATE THEM
            found_spouse_partner = mongo.db.people.find_one(
                spouse_partner_search)
            found_spouse_partner_id = found_spouse_partner["_id"]

            # ADD PERSON ID TO FOUND SPOUSE_PARTNER
            mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(found_spouse_partner_id)},
                    {"$addToSet": {"spouse_partner": persons_id}})

            # ADD FOUND SPOUSE / PARTNER TO PERSON
            mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(persons_id)},
                    {"$addToSet": {"spouse_partner": found_spouse_partner_id}})

        flash("Circle has been updated")
        return redirect(url_for(
            "edit_spouse_partner", person_id=person_id))

    return render_template(
        "edit_spouse_partner.html",
        existing_spouse_partners=existing_spouse_partners, person=person)


# ROUTE TO HANDLE ADDING OF A SIBLING
@app.route("/edit_siblings/<person_id>", methods=["GET", "POST"])
def edit_siblings(person_id):

    #   FUNCTION PURPOSE -
    #   GETS THE PERSONS SIBLING INFORMATION AND DISPLATS IT WITHIN
    #       THE TEMPLATE.
    #   ON POST -
    #   SEARCH FOR THE SIBLING ENTERED FROM THE FORM
    #   GRAB PARENTS FROM THE FORM
    #   IF SIBLING DOES NOT EXIST - CREATE IT, LINK ITS SIBLINGS,
    #       UPDATE OTHER SIBLINGS, PARENTS AND INSERT INTO PARENTS CHILDREN
    #   ELSE IF THE SIBLING DOES EXIST - LINK IT TO ITS NEW SIBLINGS,
    #       UPDATE ITS NEW SIBLINGS. UPDATE PARENTS AND UPDATE NEW AND
    #       OLD PARENTS CHILDREN

    # SETUP SOME REQUIRED VARIABLES
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    persons_id = person["_id"]
    persons_siblings_ids = person["siblings"]
    existing_siblings = {}

    # I NEED TO SEND A LIST OF POSSIBLE PARENTS TO THE TEMPLATE
    # FORCING A PARENT SELECTION WHEN ADDING A SIBLING WILL ALLOW
    # MORE ACCURATE SEARCHING WHEN TRYING TO MATCH HALF OR
    # FULL SIBLINGS AND I WANT TO DO THIS WHERE POSSIBLE
    mothers_partners_list = []
    fathers_partners_list = []
    persons_parents = []
    if person['parents']['father'] or person['parents']['father']:
        persons_parents = [
            mongo.db.people.find_one(
                {"_id": ObjectId(person['parents']['father'])}),
            mongo.db.people.find_one(
                {"_id": ObjectId(person['parents']['mother'])})
        ]

        # SETUP MOTHERS PARTNERS TO APPEND TO MOTHERS PARTNERS LIST
        mothers_partners = persons_parents[1]['spouse_partner']
        # REMOVE THE FATHER FROM PARTNERS AS HE IS ALREADY
        # ACCOUNTED FOR
        mothers_partners.remove(person['parents']['father'])
        for partner in mothers_partners:
            partner_data = mongo.db.people.find_one(
                {"_id": ObjectId(partner)})
            mothers_partners_list.append(partner_data)

        # SETUP FATHERS PARTNERS TO APPEND TO FATHERS PARTNERS LIST
        fathers_partners = persons_parents[0]['spouse_partner']
        # REMOVE THE MOTHER FROM PARTNERS AS SHE IS ALREADY
        # ACCOUNTED FOR
        fathers_partners.remove(person['parents']['mother'])
        for partner in fathers_partners:
            partner_data = mongo.db.people.find_one(
                {"_id": ObjectId(partner)})
            fathers_partners_list.append(partner_data)

    # PERSONS SIBLING - CHECK IF SIBLINGS ALREADY LINKED
    if len(persons_siblings_ids) > 0:
        # THEN PERSON HAS EXISTING SIBLINGS - SO GET THEM INTO
        # A DICT, START INDEX AT ASCII 97 'a' WAS HAVING TROUBLE WITH
        # '0' AS A KEY
        for index, sibling in enumerate(persons_siblings_ids, 97):
            existing_siblings[chr(index)] = mongo.db.people.find_one({
                "_id": ObjectId(sibling)
                })
    else:
        # WE PASS AN EMPTY DICT INTO THE TEMPLATE
        existing_siblings = {}

    # WHEN FORM IS SUBMITTED / UPDATED
    if request.method == "POST":
        # GET THE TEMPLTE FROM THE FORM FOR SIBLING
        sibling_search = {
            "first_name": request.form.get("sibling_first_name").lower(),
            "last_name": request.form.get("sibling_last_name").lower(),
            "dob": request.form.get("sibling_dob")
        }

        # GET THE 2 SELECTED PARENTS FROM THE FORM
        # EXTRACT THE 2 ID'S FROM THE RETURNED STRING
        selected_parents = {"mother": "", "father": ""}
        if len(persons_parents) != 0:
            selected_parents_in_form = request.form.get(
                "sibling_parents")
            # STRIP THE STRING DOWN TO THE ID'S
            sel_parents_string = selected_parents_in_form.replace(
                "(", "").replace(")", "").replace(
                    "'", "").replace("ObjectId", ""). replace(" ", "")
            sel_parents_array = sel_parents_string.split(",")
            selected_parents = {'mother': mongo.db.people.find_one(
                        {"_id": ObjectId(sel_parents_array[0])})['_id'],
                        'father': mongo.db.people.find_one(
                        {"_id": ObjectId(sel_parents_array[1])})['_id']}

        # SEE IF PERSON ENTERED ON FORM EXISTS
        if mongo.db.people.count_documents(sibling_search, limit=1) == 0:
            # FORM USED TO CREATE A NEW SIBLING
            sibling = {
                "family_name": person["family_name"].lower(),
                "first_name": request.form.get(
                    "sibling_first_name").lower(),
                "last_name": request.form.get("sibling_last_name").lower(),
                "birth_surname": person["birth_surname"].lower(),
                "parents": selected_parents,
                "siblings": [],
                "spouse_partner": [],
                "gender": request.form.get("gender"),
                "dob": request.form.get("sibling_dob"),
                "dod": "",
                "birth_address": "",
                "rel_address": "",
                "information": "",
                "children": []
            }
            # INSERT THE NEW SIBLING THEN GET ID:
            mongo.db.people.insert_one(sibling)
            new_sibling_id = mongo.db.people.find_one(sibling)["_id"]

            # UPDATE PERSONS SIBLING ARRAY WITH ID FROM NEW SIBLING:
            mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(person_id)},
                    {"$addToSet": {"siblings": new_sibling_id}})

            # UPDATE THE PARENTS OF THIS NEW SIBLING AS THEIR NEW CHILD:
            for key, value in selected_parents.items():
                mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(value)}, {"$addToSet": {
                        "children": new_sibling_id}})

            # BUILD LIST OF FULL OR HALF SIBLINGS.
            combined_siblings = persons_siblings_ids.copy()
            combined_siblings.append(persons_id)
            combined_siblings.append(new_sibling_id)

        else:
            #   ELSE THE SIBLING DOES EXIST IN DB, SO WE UPDATE THEM:

            #   GET THE FOUND SIBLING
            found_sibling = mongo.db.people.find_one(sibling_search)
            found_sibling_id = found_sibling["_id"]

            #   WE REMOVE THE FOUND SIBLING ID FROM ANY CHILDREN
            #       ARRAY - THIS IS BECAUSE WE ARE POSTING NEW PARENTS.
            #   FOR EXAMPLE: WE DONT WANT SIBLING HAVING 2 BIRTH MOTHERS.
            mongo.db.people.update({}, {"$pull": {
             "children": {"$in": [found_sibling_id]}}}, multi=True)

            #   WE REMOVE THE FOUND SIBLING ID FROM ANY SIBLING
            #       ARRAY - THIS IS IF THE PARENTS ARE CHANGING THEN SIBLINGS
            mongo.db.people.update({}, {"$pull": {
             "sibling": {"$in": [found_sibling_id]}}}, multi=True)

            # UPDATE THE FOUND SIBLING WITH NEW PARENTS.
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(found_sibling_id)},
                {"$set": {"parents": selected_parents}})

            # ADD FOUND SIBLING TO THE PARENTS CHILDREN ARRAY
            for key, value in selected_parents.items():
                mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(value)}, {"$addToSet": {
                        "children": found_sibling_id}})

            # SEE IF THE EXISTING SIBLING WITHIN THE DB HAS
            # ANY EXISTING SIBLINGS
            found_sibling_siblings_ids = found_sibling["siblings"]

            # NOW LOOP OVER THE FOUND SIBLING SIBLINGS ARRAY AND BUILD
            # A LIST OF THEIR OBJECT ID'S
            sibling_siblings_id_list = []
            for id in found_sibling_siblings_ids:
                obj = mongo.db.people.find_one({"_id": ObjectId(id)})
                obj_id = obj["_id"]
                sibling_siblings_id_list.append(obj_id)

            # COMBINE THESE LISTS OF SIBLINGS
            person_and_sibling_list = [persons_id, found_sibling_id]
            combined_siblings = list(set(
                person_and_sibling_list + sibling_siblings_id_list))

        #   MAKE A LIST OF SIBLINGS FOR EACH SIBLING.
        #   EACH SIBLING MUST HAVE AT LEAST ONE MATCHING PARENT
        for main_sibling in combined_siblings:
            possible_siblings = combined_siblings.copy()
            possible_siblings.remove(main_sibling)
            # HERE WE WILL CHECK TO SEE THAT ANY SIBLING IN THIS LIST
            # HAS AT LEAST ONE MATCHING PARENT.
            for sibling_in_list in possible_siblings:
                # GET THE PARENTS THE OF MAIN SIBLING IN THE LOOP
                main_sibling_data = mongo.db.people.find_one(
                    {"_id": ObjectId(main_sibling)})
                main_sibling_parents = [
                    main_sibling_data['parents']['father'],
                    main_sibling_data['parents']['mother']]
                # GET THE PARENTS OF SIBLING IN LIST
                sibling_in_list_data = mongo.db.people.find_one(
                    {"_id": ObjectId(sibling_in_list)})
                sibling_in_list_parents = [
                    sibling_in_list_data['parents']['father'],
                    sibling_in_list_data['parents']['mother']]
                # COMPARE THE PARENTS OF MAIN SIBLING AND SIBLING IN LIST
                for sibling_parent in main_sibling_parents:
                    for sib_parent in sibling_in_list_parents:
                        # IF ANY OF THE PARENTS MATCH THEN WE CAN ADD
                        # SIBLING_IN_LIST TO THE MAIN SIBLING
                        if sibling_parent == sib_parent:
                            mongo.db.people.find_one_and_update(
                                {"_id": ObjectId(main_sibling)},
                                {"$addToSet": {
                                    "siblings": sibling_in_list}})

        flash("Circle has been updated")
        return redirect(url_for(
            "edit_siblings", person_id=person_id))

    return render_template(
        "edit_siblings.html", existing_siblings=existing_siblings,
        persons_parents=persons_parents,
        mothers_partners_list=mothers_partners_list,
        fathers_partners_list=fathers_partners_list, person=person)


@app.route("/check_if_partner_exists/<person_id>")
def check_if_partner_exists(person_id):

    # FUNCTION THAT CHECKS IF PERSON BEING EDITED HAS ANY PARTNERS
    # IF YES- CONTINUE TO EDIT CHILDREN
    # IF NO - GIVE OPTION SCREEN WHAT TO DO NEXT

    # SETUP VARIABLES
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    persons_id = person["_id"]
    persons_spouse_partner_ids = person["spouse_partner"]

    # RUN THE CHECK
    if len(persons_spouse_partner_ids) > 0:
        return redirect(url_for(
            "edit_children", person_id=person_id))
    else:
        message = "This person has no spouse or partner"
        message2 = "Circles needs a person to have both parents assigned before adding children"

    return render_template("check_if_partner_exists.html", person=person, message=message, message2=message2)




# ROUTE TO HANDLE ADDING OF CHILDREN TO PERSON
@app.route("/edit_children/<person_id>", methods=["GET", "POST"])
def edit_children(person_id):

    # FUNCTION  - CHECKS FOR PERSONS EXISTING CHILDREN
    #           

    # SETUP SOME REQUIRED VARIABLES
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    persons_id = person["_id"]
    persons_gender = person["gender"]
    persons_spouse_partners_list = person["spouse_partner"]
    persons_children_ids = person["children"]
    existing_children = {}
    persons_spouse_partners = {}

    # PERSONS CHILDREN - CHECK IF CHILDREN ALREADY LINKED
    if len(persons_children_ids) > 0:
        # THEN PERSON HAS EXISTING CHILDREN - SO GET THEM INTO
        # A DICT, START INDEX AT ASCII 97 'a' WAS HAVING TROUBLE WITH
        # '0' AS A KEY
        for index, child in enumerate(persons_children_ids, 97):
            existing_children[chr(index)] = mongo.db.people.find_one({
                "_id": ObjectId(child)
                })
    else:
        # WE PASS AN EMPTY DICT INTO THE TEMPLATE
        existing_children = {}

    # PERSONS SPOUSE_PARTNER - CHECK IF SPOUSE/PARTNERS ALREADY LINKED
    if len(persons_spouse_partners_list) > 0:
        # THEN PERSON HAS EXISTING SPOUSE_PARTNERS - SO GET THEM INTO
        # A DICT, START INDEX AT ASCII 97 'a'
        for index, spouse_partner in enumerate(
                persons_spouse_partners_list, 97):
            persons_spouse_partners[chr(index)] = mongo.db.people.find_one({
                "_id": ObjectId(spouse_partner)
                })
    else:
        # PASS AN EMPTY DICT INTO THE TEMPLATE
        persons_spouse_partners = {}

    if request.method == "POST":
        # GET THE TEMPLTE FROM THE FORM FOR CHILD
        child_search = {
            "first_name": request.form.get("child_first_name").lower(),
            "last_name": request.form.get("child_last_name").lower(),
            "dob": request.form.get("child_dob")
        }

        # COMBINED SIBLINGS WILL BE USED TO CREATE THE SIBLING LINK
        # BETWEEN THIS CHILD AND ALL OTHER POSSIBLE SIBLINGS
        combined_childs_siblings = []
        persons_children = person['children']
        for item in persons_children:
            if item not in combined_childs_siblings:
                combined_childs_siblings.append(item)

        # SEE IF THE CHILD ENTERED ON FORM EXISTS
        if mongo.db.people.count_documents(child_search, limit=1) == 0:
            # THIS IS THE CASE THAT THIS ENTERED CHILD DOES NOT EXIST
            # IN THE DB. IT IS TEMPLATE WE USE TO CREATE A NEW CHILD
            child = {
                "family_name": person["family_name"].lower(),
                "first_name": request.form.get(
                    "child_first_name").lower(),
                "last_name": request.form.get("child_last_name").lower(),
                "birth_surname": person["birth_surname"].lower(),
                "parents": {"mother": "", "father": ""},
                "siblings": [],
                "spouse_partner": [],
                "gender": request.form.get("gender"),
                "dob": request.form.get("child_dob"),
                "dod": "",
                "birth_address": "",
                "rel_address": "",
                "information": "",
                "children": []
            }
            # INSERT THE NEW CHILD THEN GET ID IN CORRECT FORMAT
            mongo.db.people.insert_one(child)
            child_id = mongo.db.people.find_one(child)["_id"]
            # ADD THE NEW CHILD TO THE COMINED SIBLINGS
            combined_childs_siblings.append(child_id)

        else:
            # ELSE THE CHILD DOES EXIST IN DB, SO WE UPDATE THEM
            found_child = mongo.db.people.find_one(
                child_search)
            child_id = found_child["_id"]
            # ADD THIS FOUND CHILD TO COMBINED SIBLINGS
            if child_id not in combined_childs_siblings:
                combined_childs_siblings.append(child_id)
            # CHECK IF THIS CHILD ALREADY HAS SIBLINGS - WE WILL NEED TO
            # ADD THEM TO COMBINED SIBLINGS.
            childs_existing_siblings = found_child['siblings']
            for item in childs_existing_siblings:
                if item not in combined_childs_siblings:
                    combined_childs_siblings.append(item)

        # GET THE SELECTED OTHER PARENT
        # WE NEED TO ONLY CHECK IF THE PERSON HAS A SPOUSE
        # OR PARTNER
        selected_parent_id = False
        if len(persons_spouse_partners) != 0:
            selected_parents_in_form = request.form.get("child_parents")
            selected_parent = mongo.db.people.find_one(
                {"_id": ObjectId(selected_parents_in_form)})
            selected_parent_id = selected_parent["_id"]
            selected_parent_children = selected_parent['children']
            # ADD THIS PARENTS EXISTING CHILDREN TO THE LIST OF SIBLINGS
            for item in selected_parent_children:
                if item not in combined_childs_siblings:
                    combined_childs_siblings.append(item)

        # LINK CHILD WITH THEIR PARENTS
        child_parents = {}
        # CHECK IF PERSON IS THE MOTHER
        if persons_gender == "female":
            child_parents['mother'] = persons_id
            child_parents['father'] = ""
            if selected_parent_id:
                child_parents['father'] = selected_parent_id

        # ELSE PERSON IS THE FATHER
        elif persons_gender == "male":
            child_parents['father'] = persons_id
            child_parents['mother'] = ""
            if selected_parent_id:
                child_parents['mother'] = selected_parent_id
        else:
            child_parents = {"mother": "", "father": ""}

        # UPDATE THE CHILD WITH THEIR PARENTS
        mongo.db.people.find_one_and_update(
            {"_id": ObjectId(child_id)}, {"$set": {"parents": child_parents}})

        # UPDATE THE PERSON WITH THEIR CHILD
        mongo.db.people.find_one_and_update(
                {"_id": ObjectId(persons_id)},
                {"$addToSet": {"children": child_id}})

        # UPDATE THE PERSONS SPOUSE / PARTNER WITH THEIR CHILD
        if selected_parent_id:
            mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(selected_parent_id)},
                    {"$addToSet": {"children": child_id}})

        # COMBINE ANY CHILDREN AS SIBLINGS - CIRCLES SEES HALF OR FULL
        # SIBLINGS AS REAL SIBLINGS. SO WE NEED TO LINK THEM ALL AS SIBLINGS
        # OF EACHOTHER.
        for sibling in combined_childs_siblings:
            my_siblings = combined_childs_siblings.copy()
            my_siblings.remove(sibling)
            for add_sibling in my_siblings:
                mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(sibling)},
                    {"$addToSet": {"siblings": add_sibling}})

        flash("Circle has been updated")
        return redirect(url_for("edit_children", person_id=person_id))

    return render_template(
        'edit_children.html', persons_spouse_partners=persons_spouse_partners,
        existing_children=existing_children, person=person)


# ROUTE TO MANAGE A RELATIONSHIP
@app.route(
    "/manage_relationship/<person_id>/<person2_id>",
    methods=["GET", "POST"])
def manage_relationship(person_id, person2_id):

    # FUNCTION  - A BUFFER/CONFIRMATION HANDLER FOR THE UNLINKING
    #           - OF A PERSON FROM A SPOUSE/PARTNER
    #           - THIS FUNCTION DECIDES IF THE USER SHOULD BE ABLE
    #           - TO UNLINK A SPOUSE OR PARTNER.
    #           - UNLINK=TRUE OR FALSE IS THE KEY, TO ALLOWING
    #           - JINGA TO SHOW CORRECT OPTION

    # SETUP VARIABLES
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    person2 = mongo.db.people.find_one({"_id": ObjectId(person2_id)})
    partner_children = person2['children']
    person_children = person['children']
    unlink = False
    message = ""

    # CHECK IF PERSON HAS ANY CHILDREN - IF HE DOES
    # CHECK DO THEY MATCH ANY OF THE PARTNERS CHILDREN
    # IF THEY DO, WE MUST NOT UNLINK

    # DOES PERSON HAVE ANY CHILDREN
    if len(person_children) > 0:
        # IF YES, THEN CHECK IF ANY MATCH THE PARTNERS CHILDREN
        check = any(
            item in person_children for item in partner_children)

        # IF THERE IS A MATCH - THEN DO NOT ALLOW UNLINKING
        if check is True:
            unlink = False
            message = "These people have shared children \
                            as a result we cannot seperate them as \
                            relevant partners"
    # ELSE WE CAN ALLOW UNLINKING
    else:
        unlink = True
        message = "These people have no shared children \
                    it is safe to unlink them as relevant partners"

    return render_template(
        "manage_relationship.html", unlink=unlink, person2=person2,
        person=person, message=message)


# ROUTE TO HANDLE REMOVING A SPOUSE OR PARTNER AS A SPOUSE OR PARTNER
@app.route(
    "/delete_relationship/<person_id>/<person2_id>",
    methods=["GET", "POST"])
def delete_relationship(person_id, person2_id):

    # FUNCTION  - PERFORMS THE UNLINKING OF A
    #           - PERSON AND A SPOUSE_PARTNER

    # SETUP VARIABLES
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    person2 = mongo.db.people.find_one({"_id": ObjectId(person2_id)})
    partners_id = person2['_id']
    persons_id = person['_id']

    # PERFORM THE UNLINKING
    mongo.db.people.update({"_id": ObjectId(partners_id)}, {
        "$pull": {"spouse_partner": {"$in": [persons_id]}}})
    mongo.db.people.update({"_id": ObjectId(persons_id)}, {
        "$pull": {"spouse_partner": {"$in": [partners_id]}}})

    # RETURN PERSON_ID TO THE EDIT SPOUSE ROUTE
    flash("Relationship has been removed")
    return redirect(url_for(
            "edit_spouse_partner", person_id=person_id))

    return render_template("edit_spouse_partner.html", person_id=person_id)


@app.route("/delete_all_documents")
def delete_all_documents():
    mongo.db.people.remove({})
    flash("Circles has been Deleted")
    return render_template("home.html")


# ROUTE TO HANDLE E404
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


# TELL OUR APP, HOW AND WHERE TO RUN OUR APPLICATION
if __name__ == "__main__":
    # SET THE HOST TO THE DEFAULT IP FOUND IN ENV.PY
    app.run(host=os.environ.get("IP"),
            # CONVERT THE PORT TO AN INT
            port=int(os.environ.get("PORT")),
            # SET DEBUG TO FALSE WHEN FINISHED DEVELOPING
            debug=True)
