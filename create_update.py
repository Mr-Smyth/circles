import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from pymongo import ReturnDocument 

from bson.objectid import ObjectId


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
            "family_name": request.form.get("family_name").lower().strip(),
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


def call_create_person():

    # FUNCTION PURPOSE -
    # 1.    TO PROVIDE A TEMPLATE FOR INSERTING A NEW PERSON.

    person = {
        "family_name": request.form.get("family_name").lower().strip(),
        "first_name": request.form.get("first_name").lower().strip(),
        "last_name": request.form.get("last_name").lower().strip(),
        "birth_surname": request.form.get("birth_surname").strip(),
        "parents": {"mother": "", "father": ""},
        "siblings": [],
        "spouse_partner": [],
        "gender": request.form.get("gender").lower().strip(),
        "dob": request.form.get("dob"),
        "dod": request.form.get("dod"),
        "birth_address": request.form.get("birth_address").strip(),
        "rel_address": request.form.get("rel_address").strip(),
        "information": request.form.get("person_info").strip(),
        "children": []
    }
    return person

