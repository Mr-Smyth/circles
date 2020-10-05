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
                "spouse": "",
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

        # INSERT PERSONS MOTHER FORM DATA
        # IF PERSONS MOTHER IS NOT BLANK
        if persons_mother_id != "":
            # UPDATE MOTHERS RECORD WITH ANY CHANGE IN THE FORM TO
            # FIRST/LAST OR DOB. AND PUSH CHILD INTO CHILDREN ARRAY
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(persons_mother_id)},
                {"$addToSet": {"children": persons_id},
                 "$set": mother})
            mother_id = persons_mother_id
        else:
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
                    "spouse": "",
                    "gender": "Female",
                    "dob": request.form.get("mothers_dob"),
                    "dod": "",
                    "birth_address": "",
                    "rel_address": "",
                    "information": "",
                    "children": [persons_id]
                }
                # INSERT THE NEW MOTHER, THEN GET BACK THE ID
                new_mother = mongo.db.people.insert_one(mother)
                mother_id = new_mother.inserted_id
            else:
                # IF THE COUNT IS NOT == O, THEN WE HAVE A MATCH FOR MOTHER
                # SO WE UPDATE THAT MOTHER
                found_mother = mongo.db.people.find_one(mother)["_id"]
                mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(found_mother)},
                    {"$addToSet": {"children": persons_id},
                     "$set": mother})
                mother_id = found_mother

        # INSERT PERSONS FATHER FORM DATA
        # IF PERSONS FATHER IS NOT BLANK
        if persons_father_id != "":
            # UPDATE FATHERS RECORD WITH ANY CHANGE IN THE FORM TO
            # FIRST/LAST OR DOB. AND PUSH CHILD INTO CHILDREN ARRAY
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(persons_father_id)},
                {"$addToSet": {"children": persons_id},
                 "$set": father})
            father_id = persons_father_id
        else:
            # FIRST WE CHECK IF FATHER EXISTS ANYWHERE IN THE DB
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
                    "spouse": "",
                    "gender": "Male",
                    "dob": request.form.get("fathers_dob"),
                    "dod": "",
                    "birth_address": "",
                    "rel_address": "",
                    "information": "",
                    "children": [persons_id]
                }
                # INSERT THE NEW FATHER, THEN GET BACK THE ID
                new_father = mongo.db.people.insert_one(father)
                father_id = new_father.inserted_id
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

        flash("Circle has been updated")
        return redirect(url_for("edit_spouse_partner", person_id=person_id))

    # RETURN TO HOME, THE RESULTS CURSOR
    return render_template(
        "edit_parents.html", existing_mother=existing_mother,
        existing_father=existing_father, person=person)


# ROUTE TO HANDLE EDITING OF THE SPOUSE
@app.route("/edit_spouse_partner/<person_id>", methods=["GET", "POST"])
def edit_spouse_partner(person_id):

    # SETUP SOME REQUIRED VARIABLES
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    persons_id = person["_id"]
    persons_spouse_id = person["spouse"]

    # CHECK IF ALREADY HAVE A SPOUSE
    if persons_spouse_id != "":
        # THEN THERE IS AN EXISTING SPOUSE - SO WE ASSIGN THE ID
        existing_spouse = mongo.db.people.find_one({
            "_id": ObjectId(persons_spouse_id)})
    else:
        # ITS A NEW PERSON, SO NEW SPOUSE - IT HAS NO
        # TEMPLATE YET, SO WE GIVE IT ONE
        existing_spouse = {
                "first_name": "",
                "last_name": "",
                "dob": ""
                }

    # WHEN FORM IS SUBMITTED / UPDATED
    if request.method == "POST":
        # GET THE TEMPLTE FROM THE FORM
        # FOR SPOUSE UPDATES
        spouse = {
            "first_name": request.form.get("spouse_first_name").lower(),
            "last_name": request.form.get("spouse_last_name").lower(),
            "birth_surname": request.form.get("spouse_birth_surname").lower(),
            "spouse": persons_id,
            "dob": request.form.get("spouse_dob")
        }
        # SETUP A TEMPLATE FOR SEARCHING FOR SPOUSE - WE DONT WANT THE
        # BIRTH SURNAME FOR THIS, AS IT MAY MISS TARGET SPOUSE IF NOT
        # ALREADY ENTERED
        spouse_search = {
            "first_name": request.form.get("spouse_first_name").lower(),
            "last_name": request.form.get("spouse_last_name").lower(),
            "dob": request.form.get("spouse_dob")
        }

        # IF PERSONS SPOUSE IS NOT BLANK - THEY EXIST AS A SPOUSE
        if persons_spouse_id != "":
            # UPDATE SPOUSE RECORD WITH ANY CHANGE IN THE FORM TO
            # FIRST/LAST/MAIDEN OR DOB.
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(persons_spouse_id)},
                {"$set": spouse})
            # GRAB THE SPOUSE ID, AS WE NEED TO INSERT IT TO THE PERSON
            spouse_id = persons_spouse_id

            #UPDATE PERSON
            mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(persons_id)},
                    {"$set":{"spouse": spouse_id}})
        else:
            # FIRST WE CHECK IF SPOUSE EXISTS ANYWHERE IN THE DB
            if mongo.db.people.count_documents(spouse_search, limit=1) == 0:
                # IF THE COUNT IS == O, THEN WE INSERT A NEW SPOUSE
                spouse = {
                    "family_name": person["family_name"].lower(),
                    "first_name": request.form.get(
                        "spouse_first_name").lower(),
                    "last_name": request.form.get("spouse_last_name").lower(),
                    "birth_surname": request.form.get(
                        "spouse_last_name").lower(),
                    "parents": {"mother": "", "father": ""},
                    "siblings": [],
                    "spouse": persons_id,
                    "gender": "Female",
                    "dob": request.form.get("spouse_dob"),
                    "dod": "",
                    "birth_address": "",
                    "rel_address": "",
                    "information": "",
                    "children": []
                }
                # INSERT THE NEW SPOUSE
                inserted_spouse = mongo.db.people.insert_one(spouse)
                spouse_id = inserted_spouse.inserted_id

                # UPDATE PERSON
                mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(persons_id)},
                    {"$set": {"spouse": spouse_id}})

            else:
                # IF THE COUNT IS NOT == O, THEN WE HAVE A MATCH FOR SPOUSE
                # SO WE UPDATE THAT SPOUSE
                found_spouse = mongo.db.people.find_one(spouse_search)["_id"]
                mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(found_spouse)},
                    {"$set": spouse})
                spouse_id = found_spouse

                # UPDATE PERSON
                mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(persons_id)},
                    {"$set":{"spouse": spouse_id}})

        flash("Circle has been updated")
        return redirect(url_for(
            "edit_siblings", person_id=person_id))


    return render_template(
        "edit_spouse_partner.html", existing_spouse=existing_spouse,
        person=person)


# ROUTE TO HANDLE EDITING OF THE SIBLING
@app.route("/edit_siblings/<person_id>", methods=["GET", "POST"])
def edit_siblings(person_id):
    # SETUP SOME REQUIRED VARIABLES
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    persons_id = person["_id"]
    persons_siblings_ids = person["siblings"]
    existing_siblings = {}

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
        # GET THE TEMPLTE FROM THE FORM
        # FOR SIBLING
        sibling_search = {
            "first_name": request.form.get("sibling_first_name").lower(),
            "last_name": request.form.get("sibling_last_name").lower(),
            "dob": request.form.get("sibling_dob")
        }
        # SEE IF PERSON ENTERED ON FORM EXISTS
        if mongo.db.people.count_documents(sibling_search, limit=1) == 0:
            # THIS IS THE CASE THAT THIS ENTERED SIBLING DOES NOT EXIST
            # IN THE DB. IT IS TEMPLATE WE USE TO CREATE A NEW SIBLING
            sibling = {
                "family_name": person["family_name"].lower(),
                "first_name": request.form.get(
                    "sibling_first_name").lower(),
                "last_name": request.form.get("sibling_last_name").lower(),
                "birth_surname": person["birth_surname"].lower(),
                "parents": {"mother": "", "father": ""},
                "siblings": [],
                "spouse": "",
                "gender": request.form.get("gender"),
                "dob": request.form.get("sibling_dob"),
                "dod": "",
                "birth_address": "",
                "rel_address": "",
                "information": "",
                "children": []
            }
            # INSERT THE NEW SPOUSE THEN GET ID IN CORRECT FORMAT
            mongo.db.people.insert_one(sibling)
            new_sibling_id = mongo.db.people.find_one(sibling)["_id"]

            # UPDATE PERSONS SIBLING ARRAY WITH ID FROM NEW SIBLING
            mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(person_id)},
                    {"$addToSet": {"siblings": new_sibling_id}})

            # UPDATE PERSONS SIBLINGS WITH THIS NEW SIBLING -
            # PERSONS SIBLING + PERSONS_ID IS THE FULL SIBLING LIST
            combined_siblings = persons_siblings_ids.copy()
            combined_siblings.append(persons_id)
            combined_siblings.append(new_sibling_id)

            # ADD THIS LIST, TO ALL SIBLINGS, BUT REMOVE EACH SIBLING
            # FROM OWN LIST:
            # *     SO CREATE A MY_SIBLING_LIST - THIS LIST IS FOR ADDING
            #        TO EACH SIBLING
            # *     THEN MAKE MY_SIBLINGS EQUAL A COPY OF COMBINED SIBLINGS
            # *     THEN REMOVE CURRENT SIBLING IN THE ITERATION FROM MY
            #       SIBLINGS
            # *     ADD THE CURRENT MY_SIBLINGS TO THE ID OF THE CURRENT
            #       SIBLING IN THE ITERATION
            my_siblings = []
            for sibling in combined_siblings:
                my_siblings = combined_siblings.copy()
                my_siblings.remove(sibling)
                for add_sibling in my_siblings:
                    mongo.db.people.find_one_and_update(
                        {"_id": ObjectId(sibling)},
                        {"$addToSet": {"siblings": add_sibling}})

        else:
            # ELSE THE SIBLING DOES EXIST IN DB, SO WE UPDATE THEM
            # 1st STAGE: SEE IF THE EXISTING SIBLING WITHIN THE DB HAS
            # ANY SIBLINGS
            found_sibling = mongo.db.people.find_one(sibling_search)
            found_sibling_id = found_sibling["_id"]
            found_sibling_siblings_ids = found_sibling["siblings"]
            sibling_siblings_id_list = []

            # NOW LOOP OVER THE FOUND SIBLING SIBLINGS ARRAY AND BUILD
            # A LIST OF THEIR OBJECT ID'S
            for id in found_sibling_siblings_ids:
                obj = mongo.db.people.find_one({"_id": ObjectId(id)})
                obj_id = obj["_id"]
                sibling_siblings_id_list.append(obj_id)

            # 2nd STAGE: SEE IF PERSON HAS ANY EXISTING SIBLINGS.
            # WE HAVE THIS ALREADY SO WE USE PERSONS_SIBLINGS_IDS

            # 3RD STAGE: COMBINE THESE LISTS OF SIBLINGS
            person_and_sibling_list = [persons_id, found_sibling_id]
            combined_siblings = []
            combined_siblings = list(set(persons_siblings_ids + person_and_sibling_list + sibling_siblings_id_list))

            # 4th STAGE: PUSH EACH MY_SIBLINGS LIST TO EACH SIBLING
            # *     CREATE A MY_SIBLING_LIST - THIS LIST IS FOR ADDING TO EACH
            #       SIBLING
            # *     MAKE MY_SIBLINGS EQUAL A COPY OF COMBINED SIBLINGS
            # *     THEN REMOVE CURRENT SIBLING IN THE ITERATION FROM MY
            #       SIBLINGS
            # *     ADD THE CURRENT MY_SIBLINGS TO THE ID OF THE CURRENT
            #       SIBLING IN THE ITERATION
            my_siblings = []
            for sibling in combined_siblings:
                my_siblings = combined_siblings.copy()
                my_siblings.remove(sibling)
                for add_sibling in my_siblings:
                    mongo.db.people.find_one_and_update(
                        {"_id": ObjectId(sibling)},
                        {"$addToSet": {"siblings": add_sibling}})

        flash("Circle has been updated")
        return redirect(url_for(
            "edit_siblings", person_id=person_id))

    return render_template("edit_siblings.html", existing_siblings=existing_siblings, person=person)


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
