import os
from flask import (Flask, request)
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_pymongo import PyMongo

from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

# Setup env variables
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# Setup instance OF PyMongo
mongo = PyMongo(app)

def get_reset_token(expires_sec=1800):
    """ Creates a password reset token
    
    \n * Step 1 of password reset
    """
    current_user_id = mongo.db.users.find_one(
        {"description": 'current-user'})['current_user_id']
    
    # create a serializer object
    s = Serializer(app.secret_key, expires_sec)
    # return token created with this serializer
    # decode to utf-8
    return s.dumps({'user_id': current_user_id }).decode('utf-8')



def get_current_user():
    """Get the current logged in user
    
    \n * returns the current user object if exists
    """
    current_user = mongo.db.users.find_one(
                {"description": 'current-user'})
    return current_user


def call_search():
    """ call_search Function:

    * Build a query from user input on form.

    \n Args:
        \n None

    """
    # Get the form data
    searchInput = {
        "first_name": request.form.get("first_name").lower().strip(),
        "last_name": request.form.get("last_name").lower().strip(),
        "dob": request.form.get("dob").strip(),
    }

    # Build and return query
    query = {}
    for k, v in searchInput.items():
        if len(v) > 0:
            query[k] = v

    return query


def get_parents(person):
    """ Get parents Function:

    * Returns a list of parents objects

    \n Args:
        \n 1. person (Dict): The persons object.
    """
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
    """ Get mothers partners Function:

    * Build and return a list of mothers possible partners
      objects, not including persons father. I do this so i can display
      all possible parents of a new sibling or child.
    * When possible parents are displayed, we first show persons mum and dad
      Then we show father with each of fathers possible partners.
      Then we show mother with each of mothers possible parents.

    \n Args:
        \n 1. person (Dict): The person object.
        \n 2. persons_parents (List): A list of persons parents objects.
    """
    # Required variables
    mothers_partners_list = []

    if person['parents']['mother']:
        # Mother partners equals full list of persons mothers partners
        mothers_partners = persons_parents[1]['spouse_partner']
        # Remove persons father as he will be displayed seperately
        mothers_partners.remove(person['parents']['father'])
        for partner in mothers_partners:
            partner_data = mongo.db.people.find_one(
                {"_id": ObjectId(partner)})
            mothers_partners_list.append(partner_data)
    return mothers_partners_list


def get_fathers_partners(person, persons_parents):
    """ Get fathers partners Function:

    * Build and return a list of fathers possible partners
      objects, not including persons mother. I do this so i can display
      all possible parents of a new sibling or child.
    * When possible parents are displayed, we first show persons mum and dad
      Then we show father with each of fathers possible partners.
      Then we show mother with each of mothers possible parents.

    \n Args:
        \n 1. person (Dict): The person object.
        \n 2. persons_parents (List): A list of persons parents objects.
    """
    # Required variables
    fathers_partners_list = []

    if person['parents']['father']:
        # Fathers partners equals full list of persons fathers partners
        fathers_partners = persons_parents[0]['spouse_partner']
        # Remove persons mother as she will be displayed seperately
        fathers_partners.remove(person['parents']['mother'])
        for partner in fathers_partners:
            partner_data = mongo.db.people.find_one(
                {"_id": ObjectId(partner)})
            fathers_partners_list.append(partner_data)

    return fathers_partners_list


def build_target_list(person, target):
    """ Build target list Function:

    * Build and return a nested list of either:
     [sibling,siblings_mother,siblings_father].
    \n Or:
    * [child, childs_mother, childs_father].
    Depending on the target passed in second Arg.
    * The list is used for comparing siblings to see if they are propper
    siblings or not, which depends on them having at least one common parent.

    \n Args:
        \n 1. person (Dict): The person object.
        \n 2. target (Str): Either 'siblings' or 'children'
    """
    # Required variables
    all_targets = []

    if target == 'siblings':
        persons_target_ids = person['siblings']
        all_targets = persons_target_ids.copy()
        # All siblings should include person
        all_targets.insert(0, person['_id'])
    elif target == 'children':
        all_targets = person['children']

    # Get each target into a nested array with parents.
    target_and_parent_list = []
    # get each targets object
    for target in all_targets:
        target_object = mongo.db.people.find_one(
            {"_id": ObjectId(target)}
        )
        # Extract parents from targets object
        target_and_parent_element = []
        target_and_parent_element.append(target)
        target_and_parent_element.append(
            target_object['parents']['mother'])
        target_and_parent_element.append(
            target_object['parents']['father'])
        # Build each target, parent element into a list to return
        target_and_parent_list.append(target_and_parent_element)

    return target_and_parent_list


def merge_target_parent_list(
        found_targets_list, target_and_parent_list):
    """ Merge_target_parent_list Function:

    * Takes 2 lists:
    * The first list is a list of child or sibling id's which we will append to
    the 2nd list. It will append in the same format as the 2nd list which is:
    [person, persons_mother, persons_father]

    \n Args:
        \n 1. found_targets_list (list): list of ids i want to append to the
        list in Arg2.
        \n 2. target_and_parent_list (list): list which is correct format and
        is the list i will append to.
    """
    # Combine The 2 lists
    for target in found_targets_list:
        # Get target object so we can extract parents
        target_object = mongo.db.people.find_one(
            {"_id": ObjectId(target)}
        )
        # Extract parents and append
        target_and_parent_element = []
        target_and_parent_element.append(target)
        target_and_parent_element.append(
            target_object['parents']['mother'])
        target_and_parent_element.append(
            target_object['parents']['father'])
        # Build each element into the combined list to return
        target_and_parent_list.append(
            target_and_parent_element)

    return target_and_parent_list


def link_real_siblings(full_list):
    """ link_real_siblings Function:

    * Check list in Arg:
    * Loop over all siblings, add a list of siblings to each sibling if,
      they have at least one common parent.
    * The format of list in Arg is a nested [sibling, mother, father]

    \n Args:
        \n 1. full_list (list): A full list of siblings with parents
    """
    for this_person in full_list:
        possible_siblings = full_list.copy()
        # Remove current person as they are not a sibling of themselves
        possible_siblings.remove(this_person)
        persons_real_siblings = []

        # Check for matching parents
        for check_sibling in possible_siblings:
            if (this_person != check_sibling and
                    this_person[1] == check_sibling[1]):
                persons_real_siblings.append(
                    ObjectId(check_sibling[0]))
            elif (this_person != check_sibling and
                    this_person[2] == check_sibling[2]):
                persons_real_siblings.append(
                    ObjectId(check_sibling[0]))

        # Update each sibling
        for sibling in persons_real_siblings:
            mongo.db.people.find_one_and_update(
                {"_id": this_person[0]}, {"$addToSet": {
                    "siblings": sibling}})


def get_persons_data(person, target):
    """ get_persons_data Function:

    * Returns a list of required information,
    depending on what is entered as Arg 2.

    \n Args:
        \n 1. person (Dict): Person's Object.
        \n 2. target (Str): A String indicating req information.
        Either 'siblings', 'spouse/partner' or 'children'
    """
    # Required variables
    req_data = person[target]
    returned_data = []

    # get and return data
    if len(req_data) > 0:
        for data in req_data:
            returned_data.append(mongo.db.people.find_one({"_id": data}))

    return returned_data


def get_selected_parents(person, partners=[]):
    """ get_selected_parents Function:

    * Returns the childs parents selected from the form.

    \n Args:
        \n 1. person (Dict): Person's Object.
        \n 2. partners (Str): A list of persons spouse / partners.
    """
    # Required variables
    persons_gender = person["gender"]
    persons_id = person["_id"]
    selected_parent_id = ""
    child_parents = {}

    # Check if partners passed in is not empty
    if len(partners) != 0:
        selected_parents_in_form = request.form.get("child_parents")
        selected_parent = mongo.db.people.find_one(
            {"_id": ObjectId(selected_parents_in_form)})
        selected_parent_id = selected_parent["_id"]

        # Check if person is the mother
        if persons_gender == "female":
            child_parents['mother'] = persons_id
            child_parents['father'] = ""
            if selected_parent_id:
                child_parents['father'] = selected_parent_id

        # Else person is the father
        elif persons_gender == "male":
            child_parents['father'] = persons_id
            child_parents['mother'] = ""
            if selected_parent_id:
                child_parents['mother'] = selected_parent_id
            else:
                child_parents = {"mother": "", "father": ""}

    return child_parents


def get_chosen_parent(partners):
    """ get_chosen_parent Function:

    * Returns the id of the other parent of the child.
    Person is obviously one parent - this function gets the other.

    \n Args:
        \n 1. partners (Str): A list of persons spouse / partners.
    """

    if len(partners) != 0:
        selected_parents_in_form = request.form.get("child_parents")
        selected_parent = mongo.db.people.find_one(
            {"_id": ObjectId(selected_parents_in_form)})

    return selected_parent


def remove_all_links(persons_id):
    """ Remove person and links:

    * Remove person.
    * Remove person from any foreign arrays.

    \n Args:
        \n 1. person_id (str): The id of the person being edited.
    """
    mongo.db.people.remove({"_id": ObjectId(persons_id)})
    mongo.db.people.update({}, {"$pull": {
             "siblings": {"$in": [persons_id]}}}, multi=True)
    mongo.db.people.update({}, {"$pull": {
             "children": {"$in": [persons_id]}}}, multi=True)
    mongo.db.people.update({}, {"$pull": {
             "spouse_partner": {"$in": [persons_id]}}}, multi=True)


def remove_parent_link(person):
    """ Remove as Parent Function:

    * Because parent is an object, here we manually remove this person as a
      parent of any former children

    \n Args:
        \n 1. person (Dict): Person's Object.
    """
    persons_id = person["_id"]

    # Get the children
    children = person['children']
    children_list = []
    for child in children:
        children_list.append(mongo.db.people.find_one({
            "_id": ObjectId(child)
            }))

    # Loop over persons children, where persons id is found, remove it.
    for child in children_list:
        parents_dict = child['parents']
        for key, value in parents_dict.items():
            if value == persons_id:
                parents_dict[key] = ""
                mongo.db.people.find_one_and_update(
                    {"_id": ObjectId(child['_id'])},
                    {"$set": {"parents": parents_dict}})


def choose_sibling_parents(persons_parents):
    """ choose_sibling_parents:

    * Return a Dict of the siblings chosen parent pair.

    \n Args:
        \n 1. persons_parents (list): A list of parent objects.
    """
    # Set default parent Dict
    selected_parents = {"mother": "", "father": ""}
    # Check to make sure there are some parents
    if len(persons_parents) != 0:
        selected_parents_in_form = request.form.get(
            "sibling_parents")
        # This returned in a string so we extract the 2 object id's from it.
        sel_parents_string = selected_parents_in_form.replace(
            "(", "").replace(")", "").replace(
                "'", "").replace("ObjectId", ""). replace(" ", "")
        sel_parents_array = sel_parents_string.split(",")
        selected_parents = {'mother': mongo.db.people.find_one(
                    {"_id": ObjectId(sel_parents_array[0])})['_id'],
                    'father': mongo.db.people.find_one(
                    {"_id": ObjectId(sel_parents_array[1])})['_id']}

    return selected_parents
