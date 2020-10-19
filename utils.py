import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from pymongo import ReturnDocument 

from bson.objectid import ObjectId

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


def call_search():

    # FUNCTION PURPOSE -
    # 1.    SETUP A DICTIONARY THAT HOLDS THE INFO WE CAN QUERY
    #       IT WILL POPULATE FROM THE FORM.
    # 3.    LOOP OVER THE INPUTS TO BUILD A QUERY
    # 3.    RETURN THAT QUERY

    # GET THE SEARCH INPUTS
    searchInput = {
        "first_name": request.form.get("first_name").lower().strip(),
        "last_name": request.form.get("last_name").lower().strip(),
        "dob": request.form.get("dob").strip(),
    }

    # BUILD THE QUERY
    query = {}
    for k, v in searchInput.items():
        if len(v) > 0:
            query[k] = v

    return query


def get_parents(person):

    # FUNCTION PURPOSE -
    # 1.    TO RETURN A LIST OF THE PARENTS OBJECTS

    persons_parents = []
    if person['parents']['father'] or person['parents']['mother']:
        persons_parents = [
            mongo.db.people.find_one(
                {"_id": ObjectId(person['parents']['father'])}),
            mongo.db.people.find_one(
                {"_id": ObjectId(person['parents']['mother'])})
        ]
    return persons_parents


def get_mothers_partners(person, persons_parents):

    # FUNCTION PURPOSE -
    # 1.    TO RETURN A LIST OF THE MOTHERS POSSIBLE PARTNERS

    mothers_partners_list = []

    if person['parents']['father'] or person['parents']['mother']:
        # SETUP MOTHERS PARTNERS TO APPEND TO MOTHERS PARTNERS LIST
        mothers_partners = persons_parents[1]['spouse_partner']
        # REMOVE THE FATHER FROM PARTNERS AS HE IS ALREADY
        # ACCOUNTED FOR
        mothers_partners.remove(person['parents']['father'])
        for partner in mothers_partners:
            partner_data = mongo.db.people.find_one(
                {"_id": ObjectId(partner)})
            mothers_partners_list.append(partner_data)
    return mothers_partners_list


def get_fathers_partners(person, persons_parents):

    # FUNCTION PURPOSE -
    # 1.    TO RETURN A LIST OF THE FATHERS POSSIBLE PARTNERS

    fathers_partners_list = []

    if person['parents']['father'] or person['parents']['mother']:
        # SETUP FATHERS PARTNERS TO APPEND TO FATHERS PARTNERS LIST
        fathers_partners = persons_parents[0]['spouse_partner']
        # REMOVE THE MOTHER FROM PARTNERS AS SHE IS ALREADY
        # ACCOUNTED FOR
        fathers_partners.remove(person['parents']['mother'])
        for partner in fathers_partners:
            partner_data = mongo.db.people.find_one(
                {"_id": ObjectId(partner)})
            fathers_partners_list.append(partner_data)

    return fathers_partners_list
