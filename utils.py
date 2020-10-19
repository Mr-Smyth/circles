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


def get_persons_siblings(person):

    # FUNCTION PURPOSE -
    # 1.    TO RETURN A LIST OF THE PERSONS SIBLINGS IN OBJECT FORM

    persons_siblings_ids = person["siblings"]
    existing_siblings = []

    if len(persons_siblings_ids) > 0:
        # THEN PERSON HAS EXISTING SIBLINGS - SO GET THEM INTO A LIST
        for sib_id in persons_siblings_ids:
            existing_siblings.append(mongo.db.people.find_one({"_id": sib_id}))

    return existing_siblings


def build_target_list(person, target):

    # FUNCTION PURPOSE -
    # 1.    TO RETURN A LIST OF EITHER SIBLING, MOTHER,FATHER
    #       OR A LIST OF CHILD, MOTHER, FATHER
    #       DEPENDING ON ARGUMENT PASSED TO TARGET.
    #       - THE LIST IS USED IN COMPARING SIBLINGS OR CHILDREN
    #       TO SEE IF THEY ARE FULL OR HALF SIBLINGS

    all_targets = []

    if target == 'siblings':
        persons_target_ids = person['siblings']
        all_targets = persons_target_ids.copy()
        all_targets.insert(0, person['_id'])
    elif target == 'children':
        all_targets = person['children']

    # GET EACH TARGET AND THEIR PARENTS INTO AN ARRAY IN THE FORMAT
    # [TARGET,MOTHER,FATHER]
    target_and_parent_list = []
    # circle through sibling list as it stands
    for target in all_targets:
        # GET THE SIBLINGS OBJECT
        target_object = mongo.db.people.find_one(
            {"_id": ObjectId(target)}
        )
        # EXTRACT PARENTS FROM TARGET OBJECT
        target_and_parent_element = []
        target_and_parent_element.append(target)
        target_and_parent_element.append(
            target_object['parents']['mother'])
        target_and_parent_element.append(
            target_object['parents']['father'])
        # BUILD EACH TARGET, PARENT ELEMENT INTO LIST
        target_and_parent_list.append(target_and_parent_element)

    # AT THIS POINT TARGET_AND_PARENT_LIST IS A LIST OF ALL TARGETS
    # AND THEIR PARENTS AND WILL BE USED FOR COMPARISONS IN SIBLINGS
    # AND CHILDREN TO DETERMINE SIBLINGS

    return target_and_parent_list
