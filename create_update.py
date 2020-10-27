from flask import (request)


def blank_template():

    # FUNCTION PURPOSE -
    # 1.    TO PROVIDE A BLANK OBJECT WHEN CALLED
    #       (USUALLY REQUIRED FOR RENDERING TEMPLATES WHEN
    #       NO DATA PRESENT)

    template = {
                "first_name": "",
                "last_name": "",
                "birth_surname": "",
                "parents": {"mother": "", "father": ""},
                "siblings": [],
                "spouse_partner": [],
                "gender": "female",
                "dob": "",
                "dod": "",
                "birth_address": "",
                "rel_address": "",
                "information": "",
                "children": []
            }
    return template


def call_person_update():

    # FUNCTION PURPOSE -
    # 1.    TO PROVIDE AN UPDATE TEMPLATE FOR UPDATING A PERSON

    person_update = {
            "family_name": 'My Circle',
            "first_name": request.form.get("first_name").lower().strip(),
            "last_name": request.form.get("last_name").lower().strip(),
            "birth_surname": request.form.get("birth_surname").strip(),
            "gender": request.form.get("gender").lower().strip(),
            "dob": request.form.get("dob"),
            "dod": request.form.get("dod"),
            "birth_address": request.form.get("birth_address").strip(),
            "rel_address": request.form.get("rel_address").strip(),
            "information": request.form.get("person_info"),
        }
    return person_update


def call_create_person(
    person={"family_name": "My Circle"}, parents={
        "mother": "", "father": ""}):

    # FUNCTION PURPOSE -
    # 1.    TO PROVIDE A TEMPLATE OBJECT FOR INSERTING A NEW PERSON.

    # setup some variable for forms that do not contain all required fields
    if person['family_name']:
        family_name = person['family_name']
    else:
        family_name = "My Circle"
    if request.form.get("birth_surname"):
        birth_surname = request.form.get("birth_surname").strip()
    else:
        birth_surname = ""
    if request.form.get("dob"):
        dob = request.form.get("dob").strip()
    else:
        dob = ""
    if request.form.get("dod"):
        dod = request.form.get("dod").strip()
    else:
        dod = ""
    if request.form.get("birth_address"):
        birth_address = request.form.get("birth_address").strip()
    else:
        birth_address = ""

    if request.form.get("rel_address"):
        rel_address = request.form.get("rel_address").strip()
    else:
        rel_address = ""

    if request.form.get("information"):
        information = request.form.get("information").strip()
    else:
        information = ""

    person = {
        "family_name": family_name,
        "first_name": request.form.get("first_name").lower().strip(),
        "last_name": request.form.get("last_name").lower().strip(),
        "birth_surname": birth_surname,
        "parents": parents,
        "siblings": [],
        "spouse_partner": [],
        "gender": request.form.get("gender").lower().strip(),
        "dob": dob,
        "dod": dod,
        "birth_address": birth_address,
        "rel_address": rel_address,
        "information": information,
        "children": []
    }
    return person


def create_parent(person, parent):

    # FUNCTION PURPOSE -
    # 1.    RETURN A PARENT TEMPLATE TO CREATE A NEW PARENT

    if parent == 'mother':
        mother = {
                    "family_name": 'My Circle',
                    "first_name": request.form.get(
                        "mothers_first_name").lower().strip(),
                    "last_name": request.form.get(
                        "mothers_last_name").lower().strip(),
                    "birth_surname": "",
                    "parents": {"mother": "", "father": ""},
                    "siblings": [],
                    "spouse_partner": [],
                    "gender": "female",
                    "dob": request.form.get("mothers_dob").strip(),
                    "dod": "",
                    "birth_address": "",
                    "rel_address": "",
                    "information": "",
                    "children": []
                }
        return mother

    if parent == 'father':
        father = {
                "family_name": 'My Circle',
                "first_name": request.form.get(
                    "fathers_first_name").lower().strip(),
                "last_name": request.form.get(
                    "fathers_last_name").lower().strip(),
                "birth_surname": "",
                "parents": {"mother": "", "father": ""},
                "siblings": [],
                "spouse_partner": [],
                "gender": "male",
                "dob": request.form.get("fathers_dob"),
                "dod": "",
                "birth_address": "",
                "rel_address": "",
                "information": "",
                "children": []
                }
        return father
