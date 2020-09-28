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
            "parents": {"mum": "not_defined", "dad": "not_defined"},
            "siblings": "not_defined",
            "spouse": "not_defined",
            "gender": request.form.get("gender"),
            "dob": request.form.get("dob"),
            "dod": request.form.get("dod"),
            "birth_address": request.form.get("birth_address"),
            "rel_address": request.form.get("rel_address"),
            "information": request.form.get("person_info")
        }
        # ADD THE PERSON DICTIONARY TO MONGO
        mongo.db.people.insert_one(person)
        flash("This Person has bees successfully added to Circles")
        return redirect(url_for("home"))
    
    # GET THE FAMILY COLLECTION NAMES, FOR THE FAMILY
    # SELECTION DROP DOWN
    families = mongo.db.family.find().sort("family_name",1)
    # RETURN THE FAMILIES TO THE ADD_PERSON PAGE FOR JINGA
    return render_template("add_person.html", families=families)


# EDIT PARENTS ROUTE AND FUNCTION
@app.route("/edit_parents/<person_id>", methods=["GET", "POST"])
def edit_parents(person_id):
    # IN EDIT PERSON, WE WILL REFER TO PERSON AS THE HUB_PERSON
    # THIS FUNCTION WILL 
    # * CHECK IF ENTERED MOTHER AND FATHER ARE ALREADY IN DB
    # * DISPLAY CURRENT PARENTS
    # * CHANGE THE PARENTS IF NEW PARENTS ENTERED

    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})
    # GET FATHERS INFO
    existing_mother_id = person["parents"]["mother"]
    existing_mother = mongo.db.people.find_one({"_id": ObjectId(existing_mother_id)})

    # GET MOTHERS INFO
    existing_father_id = person["parents"]["father"]
    existing_father = mongo.db.people.find_one({"_id": ObjectId(existing_father_id)})

    if request.method == "POST":

        # SETUP A DICTIONARY THAT HOLDS THE INFOR WE CAN QUERY
        # IT WILL POPULATE FROM THE FORM.
        mother = {
        "first_name": request.form.get("mothers_first_name").lower(),
        "last_name": request.form.get("mothers_last_name").lower(),
        "dob": request.form.get("mothers_dob"),
        }
        father = {
        "first_name": request.form.get("fathers_first_name").lower(),
        "last_name": request.form.get("fathers_last_name").lower(),
        "dob": request.form.get("fathers_dob"),
        }

        # SETUP A BLANK QUERY DICTIONARY AND THEN LOOP OVER
        # mother and father ABOVE TO BUILD A QUERY.
        # TO CHECK IF THEY ARE ALREADY IN MONGODB
        query_mother = {}
        for k,v in mother.items():
            if len(v) > 0:    
                query_mother[k] = v

        query_father = {}
        for k,v in father.items():
            if len(v) > 0:    
                query_father[k] = v
        
        father_exists = list(mongo.db.people.find(query_father))
        mother_exists = list(mongo.db.people.find(query_mother))

        hub_person_id = person_id
        hub_mother_id = ""
        hub_father_id = ""
        parents = {"parents": {"mother": "not_defined", "father": "not_defined"}}
        
        # PREP INSERT TEMPLATE FOR MOTHER
        insert_father = {
            "family_name": person["family_name"].lower(),
            "first_name": query_father["first_name"].lower(),
            "last_name": query_father["last_name"].lower(),
            "birth_surname": "not_defined",
            "parents": {"mum": "not_defined", "dad": "not_defined"},
            "siblings": "not_defined",
            "spouse": "not_defined",
            "children": [hub_person_id],
            "gender": "male",
            "dob": query_father['dob'],
            "dod": "not-defined",
            "birth_address": "not_defined",
            "rel_address": "not_defined",
            "information": "not_defined"
        }
        # PREP INSERT TEMPLATE FOR A NEW FATHER
        insert_mother = {
            "family_name": person["family_name"].lower(),
            "first_name": query_mother["first_name"].lower(),
            "last_name": query_mother["last_name"].lower(),
            "birth_surname": "not_defined",
            "parents": {"mum": "not_defined", "dad": "not_defined"},
            "siblings": "not_defined",
            "spouse": "not_defined",
            "children": [hub_person_id],
            "gender": "female",
            "dob": query_mother["dob"],
            "dod": "not-defined",
            "birth_address": "not_defined",
            "rel_address": "not_defined",
            "information": "not_defined"
        }

        # IF HUB PERSONS MOTHER ALREADY EXISTS
        if mother_exists:
            # SET THE MOTHER_EXISTS AS THE HUB MOTHER
            hub_mother = mother_exists
            # NOW WE NEED THE ID OF THAT MOTHER
            for field in mother_exists:
                hub_mother_id = field['_id']
            # NOW UPDATE THAT HUB MOTHER WITH THE SAME INSERT_MOTHER
            # BUT SKIP OVER THE NOT_DEFINED VALUES
            for k, v in insert_mother.items():
                if v != "not_defined":
                    insert = {}
                    insert[k] = v
                    mongo.db.people.update({"_id": ObjectId(
                        hub_mother_id)}, insert_mother)
                    parents["parents"]["mother"] = hub_mother_id

        else:
            # ELSE WE INSERT THE ONE ENTERED BY THE USER
            newMother = mongo.db.people.insert_one(insert_mother)
            # AND GET BACK ITS NEW ID
            hub_mother_id = newMother.inserted_id
            parents["parents"]["mother"] = hub_mother_id

        # IF HUB PERSONS FATHER ALREADY EXISTS
        if father_exists:
            # SET THE FATHER EXISTS AS THE HUB FATHER
            hub_father = father_exists
            # NOW WE NEED THE ID OF THAT FATHER
            for field in father_exists:
                hub_father_id = field['_id']
            # NOW UPDATE THAT HUB FATHER WITH THE SAME INSERT_FATHER
            # BUT SKIP OVER THE NOT_DEFINED VALUES
            for k,v in insert_father.items():
                if v != "not_defined":
                    insert = {}
                    insert[k] = v
                    mongo.db.people.update({"_id": ObjectId(
                        hub_father_id)}, insert_father)
                    parents["parents"]["father"] = hub_father_id
        else:
            # ELSE WE INSERT THE ONE ENTERED BY THE USER
            newFather = mongo.db.people.insert_one(insert_father)
            # AND GET BACK THE NEW ID
            hub_father_id = newFather.inserted_id
            parents["parents"]["father"] = hub_father_id

        # SO NOW PARENTS ARE ASSIGNED, WE CAN UPDATE OUR HUB PERSON WITH THEIR PARENTS
        mongo.db.people.update_one({"_id": ObjectId(hub_person_id)}, {"$set": parents})

        flash("Eamonn has been updated")
        return redirect(url_for("edit_parents", person_id=person_id))


        # RETURN TO HOME, THE RESULTS CURSOR
    return render_template("edit_parents.html", existing_mother=existing_mother, existing_father=existing_father, person=person)








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
