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


def build_target_list(person, target):

    # FUNCTION PURPOSE -
    # 1.    TO RETURN A LIST OF EITHER SIBLING, MOTHER,FATHER
    #       OR A LIST OF CHILD, MOTHER, FATHER
    #       DEPENDING ON ARGUMENT PASSED TO TARGET.
    #       - THE LIST IS USED IN COMPARING SIBLINGS OR CHILDREN
    #       TO SEE IF THEY ARE FULL OR HALF SIBLINGS
    # 2.    USED FOR SIBLINGS AND CHILDREN, HENCE GENERAL NAME OF TARGET

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


def merge_target_parent_list(
        found_targets_list, target_and_parent_list):

    # FUNCTION PURPOSE -
    # 1.    COMBINE THE 2 LISTS INTO A LIST OF THE FORMAT
    #       [ [ TARGET, MOTHER, FATHER ], [ TARGET, MOTHER, FATHER ] ]
    #       THIS WILL SERVE BOTH ASSIGN SIBLINGS AND ALSO ASSIGN CHILDREN

    for target in found_targets_list:
        # GET THE TARGETS OBJECT
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
        target_and_parent_list.append(
            target_and_parent_element)

    return target_and_parent_list


def link_real_siblings(full_list):

    # FUNCTION PURPOSE -
    # 1.    CHECK OVER THIS COMPLETE LIST OF SIBLINGS
    #       CHECK IF AT LEAST ONE PARENT MATCHES, IF A PARENT
    #       MATCHES WE CAN ADD AS A SIBLING, ELSE - NOT A SIBLING.
    #       THIS IS NEEDED BECAUSE SOME SIBLINGS MAY HAVE HALF SIBLINGS
    #       NOT RELATED TO NEW SIBLINGS

    for this_person in full_list:
        # THIS_PERSON IS AN ELEMENT CONTAINING
        # [SIBLING, MOTHER, FATHER]

        possible_siblings = full_list.copy()
        # REMOVE THIS PERSON SO WE DONT MAKE THEM A SIBLING OF THEMSELVES
        possible_siblings.remove(this_person)
        persons_real_siblings = []

        # CHECK FOR MATCHING PARENTS
        for check_sibling in possible_siblings:
            if (this_person != check_sibling and
                    this_person[1] == check_sibling[1]):
                persons_real_siblings.append(
                    ObjectId(check_sibling[0]))
            elif (this_person != check_sibling and
                    this_person[2] == check_sibling[2]):
                persons_real_siblings.append(
                    ObjectId(check_sibling[0]))

        # UPDATE EACH SIBLING
        for sibling in persons_real_siblings:
            mongo.db.people.find_one_and_update(
                {"_id": this_person[0]}, {"$addToSet": {
                    "siblings": sibling}})


def get_persons_data(person, target):

    # FUNCTION PURPOSE -
    # 1.    TO RETURN A LIST OF THE PERSONS - WHATEVER IS IN 'target' IN
    #       OBJECT FORM

    req_data = person[target]
    returned_data = []

    if len(req_data) > 0:
        # THEN PERSON HAS EXISTING SIBLINGS - SO GET THEM INTO A LIST
        for data in req_data:
            returned_data.append(mongo.db.people.find_one({"_id": data}))

    return returned_data


def get_selected_parents(person, partners=[]):

    persons_gender = person["gender"]
    persons_id = person["_id"]
    selected_parent_id = ""
    child_parents = {}
    # CHECK THAT PARTNERS IS NOT EMPTY
    if len(partners) != 0:
        selected_parents_in_form = request.form.get("child_parents")
        selected_parent = mongo.db.people.find_one(
            {"_id": ObjectId(selected_parents_in_form)})
        selected_parent_id = selected_parent["_id"]

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

    return child_parents


def get_chosen_parent(partners):

    # FUNCTION PURPOSE -
    # 1.    RETURN THE ID OF THE PARENT(OTHER THAN THE PERSON)
    #       SELECTED IN THE FORM

    if len(partners) != 0:
        selected_parents_in_form = request.form.get("child_parents")
        selected_parent = mongo.db.people.find_one(
            {"_id": ObjectId(selected_parents_in_form)})

    return selected_parent


def remove_all_links(persons_id):

    # FUNCTION PURPOSE -
    # 1.    REMOVE THE PERSONS ID FROM ANY RELATED ARRAYS IN THE COLLECTION

    mongo.db.people.remove({"_id": ObjectId(persons_id)})
    mongo.db.people.update({}, {"$pull": {
             "siblings": {"$in": [persons_id]}}}, multi=True)
    mongo.db.people.update({}, {"$pull": {
             "children": {"$in": [persons_id]}}}, multi=True)
    mongo.db.people.update({}, {"$pull": {
             "spouse_partner": {"$in": [persons_id]}}}, multi=True)


def remove_parent_link(person):

    # FUNCTION PURPOSE -
    # 1.    BECAUSE CHILDREN HAVE A LINK TO A PARENT VIA AN OBJECT
    #       HERE I GET EACH PARENTS OBJECT AND REMOVE THE ID OF THE
    #       PERSON WE ARE REMOVING.

    persons_id = person["_id"]

    #       GET CHILDREN
    children = person['children']
    children_list = []
    for child in children:
        children_list.append(mongo.db.people.find_one({
            "_id": ObjectId(child)
            }))

    # LOOP OVER THE LIST OF CHILDREN AND CHECK FOR A
    # MATCHING ID, IF FOUND REPLACE WITH DEFAULT "".
    # THEN UPDATE THAT CHILD.
    for child in children_list:
        parents_dict = child['parents']
        for key, value in parents_dict.items():
            if value == persons_id:
                parents_dict[key] = ""
                mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(child['_id'])},
                    {"$set": {"parents": parents_dict}})
