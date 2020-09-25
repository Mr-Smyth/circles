# Manual ContinuousTesting
(all Initial/continuous testing performed between Google Chrome and a Samsung Galaxy S7. Individual browser tests will be performed after main development stage)

# Index

* [Test the initial setup connection to Heroku](#test-connection-to-heroku)
* [Testing of Home page](#testing-of-home-page)
* [Testing of Search Functionality](#testing-of-search-functionality)
* [Testing of Add Person Functionality](#testing-of-add-person-functionality)


---
## Test connection to Heroku.

#### After the initial setup of the flask app, and adding the relevent enviroment variables, and deployment to Heroku i performed the following tests.

* :hammer: TEST:	
    * Setup a base route and function and entered a simple return text "This is Circles".
* :equal: RESULT: 
    * The result displayed as expected on the local development server.
	* The result displayed as expected on the deployed site via Heroku.

[Back to Index](#index)

---

## Testing of Home page:

### Initial visual tests:

#### After initial layout and setup of basic navbar and logo, i performed the following tests

* TEST: 
    * Viewed Page on various screen sizes to check for overflow and undesired behavior
* RESULT: 
    * The home page rendered as expected.
	* The resposiveness was good for initial testing.


[Back to Index](#index)

---

## Testing of Search Functionality:

## Initial Testing:

#### After the initial setup of the search functionality, i decided to move from a single full name search box to a more flexible Mini Form.
I believ this gave me the experience that was more flexible and desirable, in that i could search by any of First name, last name or DOB, or all together.

* TEST: 
    * Provided a name in mixed case to the first name only.
* RESULT:
    * All results for that name, returned from MongoDB as expected.

<br>

* TEST:
    * Provided a name in mixed case to the last name only.
* RESULT:
    * All results for that name, returned from MongoDB as expected.

<br>

* TEST:
    * Provided a DOB only.
* RESULT:   
    * All results for that DOB, returned from MongoDB as expected.

<br>

* TEST:
    * Provided a name in mixed case to the first name, last name and selected a DOB.
* RESULT: 
    * Results for that name, and DOB returned from MongoDB as expected.
	* Results were filtered down to reflect the more detailed search.

Visually all results were displayed in a colapsible element, which was otherwise hidden

### In the case of Errors:

* TEST: 
    * Provided a name to the name fields that was not in the Mongo collection.
* RESULT:   
    * The error message passed into the home template from the search function, was succesfully displayed in bold.

This did not freeze or break the site, and allowed the user to click on the search button, and attempt another search. The message reflected the error.

## Final Testing:

[Back to Index](#index)

---

## Testing of Add Person Functionality:

## Initial Testing:

#### After the initial setup of the Add person functionality, i performed the following tests

* TEST: 
    * Entered information into all fields in search form, and submitted
* RESULT:
    * A Flash message to inform the user that the person was inserted successfully was displayed.
    * The Mongo collection contained 2 problems:
* ERRORS: 
	* Where i had not matched the import dictionary with the correct HTML input ID, the type of the document was set to null.
* FIX: 
	* I matched the import field in the dictionary being imported, to the correct Id in the form.

* RE-TESTED RESULT: 
	* All fields within each document in MongoDB were inserted correctly.

<br>

* TEST:
    * Make sure i could not enter dates manually
* RESULT:
    * No dates can be entered manually.

<br>

* TEST:
    * What happens when i try to submit an empty form
* RESULT:   
    * In form validation, using required, ensures that a minimum of somones Umbrella family Circle name, First name, Last name and Date of birth is required.

<br>

* TEST:
    * Could i recall all the information from a document
* RESULT: 
    * Using the search feature on the home page, i was able to recall and view any document i entered.



## Final Testing:

[Back to Index](#index)

---