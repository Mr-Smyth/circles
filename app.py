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
    if len(query) != 0:
        results = list(mongo.db.people.find(query))
    else:
        return redirect(url_for("home"))
    
    # RETURN TO HOME, THE RESULTS CURSOR
    return render_template("home.html", results=results)




# ADD PERSON ROUTE
@app.route("/add_person", methods=["GET", "POST"])
def add_person():




    if request.method == "POST":
        # SETUP DICTIONARY FOR IMPORTING PERSON TO MONGO DB
        person = {
            "family_name": request.form.get("family_name"),
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "birth_surname": request.form.get("birth_surname"),
            "gender": request.form.get("gender"),
            "dob": request.form.get("dob"),
            "dod": request.form.get("dod"),
            "birth_address": request.form.get("birth_address"),
            "rel_address": request.form.get("rel_address"),
            "info": request.form.get("info")
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


# TELL OUR APP, HOW AND WHERE TO RUN OUR APPLICATION
if __name__ == "__main__":
    # SET THE HOST TO THE DEFAULT IP FOUND IN ENV.PY
    app.run(host=os.environ.get("IP"),
            # CONVERT THE PORT TO AN INT
            port=int(os.environ.get("PORT")),
            # SET DEBUG TO FALSE WHEN FINISHED DEVELOPING
            debug=True)
