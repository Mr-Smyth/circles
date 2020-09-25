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
            "parents": "null",
            "siblings": "null",
            "spouse": "null",
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

    person = mongo.db.people.find_one({"_id": ObjectId(person_id)})

    return render_template("edit_parents.html", person=person)



@app.route("/add_parents/<person_id>", methods=["GET", "POST"])
def add_parents(person_id):
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
        
        existing_father = list(mongo.db.people.find(query_father))
        existing_mother = list(mongo.db.people.find(query_mother))

        # GET PERSON WHO WE ARE CONNECTING PARENTS TO
        person = mongo.db.people.find_one({"_id": ObjectId(person_id)})

        hub_person_id = person_id
        hub_mother_id = ""
        hub_father_id = ""
        
        insert_father = {
            "family_name": person["family_name"],
            "first_name": query_father["first_name"],
            "last_name": query_father["last_name"],
            "birth_surname": "null",
            "parents": "null",
            "siblings": "null",
            "spouse": "null",
            "children": [hub_person_id],
            "gender": "male",
            "dob": query_father['dob'],
            "dod": "null",
            "birth_address": "null",
            "rel_address": "null",
            "information": "null"
        }
        insert_mother = {
            "family_name": person["family_name"],
            "first_name": query_mother["first_name"],
            "last_name": query_mother["last_name"],
            "birth_surname": "null",
            "parents": "null",
            "siblings": "null",
            "spouse": "null",
            "children": [hub_person_id],
            "gender": "female",
            "dob": query_mother["dob"],
            "dod": "null",
            "birth_address": "null",
            "rel_address": "null",
            "information": "null"
        }

        # IF HUB PERSONS MOTHER ALREADY EXISTS
        if existing_mother:
            # SET THE EXISTING MOTHER AS THE HUB MOTHER
            hub_mother = existing_mother
            # NOW WE NEED THE ID OF THAT MOTHER
            for field in existing_mother:
                hub_mother_id = field['_id']
        else:
            # ELSE WE INSERT THE ONE ENTERED BY THE USER
            x = mongo.db.people.insert_one(insert_mother)
            # AND GET BACK ITS NEW ID
            hub_mother_id = x.inserted_id

        # IF HUB PERSONS FATHER ALREADY EXISTS
        if existing_father:
            # SET THE EXISTING FATHER AS THE HUB FATHER
            hub_father = existing_father
            # NOW WE NEED THE ID OF THAT FATHER
            for field in existing_father:
                hub_father_id = field['_id']

        else:
            # ELSE WE INSERT THE ONE ENTERED BY THE USER
            x = mongo.db.people.insert_one(insert_father)
            # AND GET BACK THE NEW ID
            hub_father_id = x.inserted_id




        # RETURN TO HOME, THE RESULTS CURSOR
    return render_template("edit_parents.html", hub_father_id=hub_father_id, hub_mother_id=hub_mother_id, hub_person_id=hub_person_id, person=person )


# TELL OUR APP, HOW AND WHERE TO RUN OUR APPLICATION
if __name__ == "__main__":
    # SET THE HOST TO THE DEFAULT IP FOUND IN ENV.PY
    app.run(host=os.environ.get("IP"),
            # CONVERT THE PORT TO AN INT
            port=int(os.environ.get("PORT")),
            # SET DEBUG TO FALSE WHEN FINISHED DEVELOPING
            debug=True)
