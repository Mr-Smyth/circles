import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo

from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

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
        for k,v in searchInput.items():
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
@app.route("/add_person", methods=["GET", "POST"])
def add_person():

    if request.method == "POST":
        # SETUP DICTIONARY FOR IMPORTING PERSON TO MONGO DB
        person = {
            "family_name": request.form.get("family_name").lower(),
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "birth_surname": request.form.get("birth_surname"),
            "parents": {"mother": "", "father": ""},
            "siblings": "",
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
        new_person = mongo.db.people.insert_one(person)
        flash("This Person has bees successfully added to Circles")
        return redirect(url_for("edit_parents", person_id=new_person.inserted_id))
    
    # GET THE FAMILY COLLECTION NAMES, FOR THE FAMILY
    # SELECTION DROP DOWN
    families = mongo.db.family.find().sort("family_name",1)
    # RETURN THE FAMILIES TO THE ADD_PERSON PAGE FOR JINGA
    return render_template("add_person.html", families=families)


# EDIT PARENTS ROUTE AND FUNCTION
@app.route("/edit_parents/<person_id>", methods=["GET", "POST"])
def edit_parents(person_id):
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    persons_id = person["_id"]
    persons_mother_id = person["parents"]["mother"]
    persons_father_id = person["parents"]["father"]

    # person's mother
    if persons_mother_id != "":
        # has existing mother
        existing_mother = mongo.db.people.find_one({"_id": ObjectId(persons_mother_id)})
    else:
        # new profile, no mother yet
        existing_mother = {"first_name": "", "last_name": "", "dob": ""}

    # person's father
    if persons_father_id != "":
        # has existing father
        existing_father = mongo.db.people.find_one({"_id": ObjectId(persons_father_id)})
    else:
        # new profile, no father yet
        existing_father = {"first_name": "", "last_name": "", "dob": ""}

    # form being updated/submitted
    if request.method == "POST":
        mother = {
            "first_name": request.form.get("mothers_first_name").lower(),
            "last_name": request.form.get("mothers_last_name").lower(),
            "dob": request.form.get("mothers_dob")
        }
        father = {
            "first_name": request.form.get("fathers_first_name").lower(),
            "last_name": request.form.get("fathers_last_name").lower(),
            "dob": request.form.get("fathers_dob")
        }

        # insert mother's form data
        if persons_mother_id != "":
            # update mother's record with any change to first/last/dob + push child to array
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(persons_mother_id)},
                {"$addToSet": {"children": persons_id},
                "$set": mother})
            mother_id = persons_mother_id
        else:
            # first check if mother already exists in db
            if mongo.db.people.count_documents(mother, limit=1) == 0:
                # add new record for person's mother
                mother = {
                    "family_name": person["family_name"].lower(),
                    "first_name": request.form.get("mothers_first_name").lower(),
                    "last_name": request.form.get("mothers_last_name").lower(),
                    "birth_surname": "",
                    "parents": {"mother": "", "father": ""},
                    "siblings": "",
                    "spouse": "",
                    "gender": "Female",
                    "dob": request.form.get("mothers_dob"),
                    "dod": "",
                    "birth_address": "",
                    "rel_address": "",
                    "information": "",
                    "children": [persons_id]
                }
                new_mother = mongo.db.people.insert_one(mother)
                mother_id = new_mother.inserted_id
            else:
                # found a match for existing mother, so update accordingly
                found_mother = mongo.db.people.find_one(mother)["_id"]
                mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(found_mother)},
                    {"$addToSet": {"children": persons_id},
                    "$set": mother})
                mother_id = found_mother

        # insert father's form data
        if persons_father_id != "":
            # update father's record with any change to first/last/dob + push child to array
            mongo.db.people.find_one_and_update(
                {"_id": ObjectId(persons_father_id)},
                {"$addToSet": {"children": persons_id},
                "$set": father})
            father_id = persons_father_id
        else:
            # first check if father already exists in db
            if mongo.db.people.count_documents(father, limit=1) == 0:
                # add new record for person's father
                father = {
                    "family_name": person["family_name"].lower(),
                    "first_name": request.form.get("fathers_first_name").lower(),
                    "last_name": request.form.get("fathers_last_name").lower(),
                    "birth_surname": "",
                    "parents": {"mother": "", "father": ""},
                    "siblings": "",
                    "spouse": "",
                    "gender": "Male",
                    "dob": request.form.get("fathers_dob"),
                    "dod": "",
                    "birth_address": "",
                    "rel_address": "",
                    "information": "",
                    "children": [persons_id]
                }
                new_father = mongo.db.people.insert_one(father)
                father_id = new_father.inserted_id
            else:
                # found a match for existing father, so update accordingly
                found_father = mongo.db.people.find_one(father)["_id"]
                mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(found_father)},
                    {"$addToSet": {"children": persons_id},
                    "$set": father})
                father_id = found_father

        # update person's parent's details
        parents = {"mother": mother_id, "father": father_id}
        mongo.db.people.find_one_and_update({"_id": ObjectId(person_id)}, {"$set": {"parents": parents}})

        flash("Circle has been updated")
        return redirect(url_for("edit_parents", person_id=person_id))

    # RETURN TO HOME, THE RESULTS CURSOR
    return render_template("edit_parents.html", existing_mother=existing_mother, existing_father=existing_father, person=person)


# ROUTE TO HANDLE EDITING OF THE MAIN HUB PERSON
@app.route("/edit_hub_person/<person_id>", methods=["GET", "POST"])
def edit_hub_person(person_id):
    # GET THE HUB_PERSON INFO
    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    return render_template("edit_hub_person.html", person=person)




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
