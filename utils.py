import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from pymongo import ReturnDocument 

from bson.objectid import ObjectId


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
