# Manual ContinuousTesting
(all Initial/continuous testing performed between Google Chrome and a Samsung Galaxy S7. Individual browser tests will be performed after main development stage)

# Index

* [Test the initial setup connection to Heroku](#test-connection-to-heroku)
* [Testing of Home page](#testing-of-home-page)
* [Testing of Search Functionality](#testing-of-search-functionality)
* [Testing of Add Person Functionality](#testing-of-add-person-functionality)
* [Testing of Edit Parents Functionality](#testing-of-edit-parents-functionality)
* [Testing of Add Spouse or Partner Functionality](#testing-of-edit-spouse-functionality)
* [Testing of Add Sibling Functionality](#testing-of-edit-siblings-functionality)
* [Testing of Check for Spouse Functionality](#testing-of-check-for-spouse-functionality)
* [Testing of Add Children Functionality](#testing-of-edit-children-functionality)


---
## Test connection to Heroku.

#### After the initial setup of the flask app, and adding the relevent enviroment variables, and deployment to Heroku i performed the following tests.

* :hammer: TEST:	
    * Setup a base route and function and entered a simple return text "This is Circles".
* :clipboard: RESULT: 
    * The result displayed as expected on the local development server.
	* The result displayed as expected on the deployed site via Heroku.

### Final Testing:

#### After the development stage, i performed the following tests

* :hammer: TEST: 
    * Test here..
* :clipboard: RESULT:
    * Results here

[Back to Index](#index)

---

## Testing of Home page:

### Initial visual tests:

#### After initial layout and setup of basic navbar and logo, i performed the following tests

* :hammer: TEST: 
    * Viewed Page on various screen sizes to check for overflow and undesired behavior
* :clipboard: RESULT: 
    * The home page rendered as expected.
	* The resposiveness was good for initial testing.

<br>

* :hammer: TEST: 
    * Clicked the search input
* :clipboard: RESULT:
    * The search input dissappeared and the search form appeared. All displayed as expected.

*In all cases the pages styling rendered as expected on both mobile, tablet and desktop.*

### Final Testing:

#### After the development stage, i performed the following tests

* :hammer: TEST: 
    * Test here..
* :clipboard: RESULT:
    * Results here

[Back to Index](#index)

---

## Testing of Search Functionality:

### Initial Testing:

#### After the initial setup of the search functionality, i decided to move from a single full name search box to a more flexible Mini Form.
I believ this gave me the experience that was more flexible and desirable, in that i could search by any of First name, last name or DOB, or all together.

* :hammer: TEST: 
    * Provided a name in mixed case to the first name only.
* :clipboard: RESULT:
    * All results for that name, returned from MongoDB as expected.

<br>

* :hammer: TEST:
    * Provided a name in mixed case to the last name only.
* :clipboard: RESULT:
    * All results for that name, returned from MongoDB as expected.

<br>

* :hammer: TEST:
    * Provided a DOB only.
* :clipboard: RESULT:   
    * All results for that DOB, returned from MongoDB as expected.

<br>

* :hammer: TEST:
    * Provided a name in mixed case to the first name, last name and selected a DOB.
* :clipboard: RESULT: 
    * Results for that name, and DOB returned from MongoDB as expected.
	* Results were filtered down to reflect the more detailed search.

Visually all results were displayed in a colapsible element, which was otherwise hidden

### In the case of Errors:

* :hammer: TEST: 
    * Provided a name to the name fields that was not in the Mongo collection.
* :clipboard: RESULT:   
    * The error message passed into the home template from the search function, was succesfully displayed in bold.

This did not freeze or break the site, and allowed the user to click on the search button, and attempt another search. The message reflected the error.

*In all cases the pages styling rendered as expected on both mobile, tablet and desktop.*

### Final Testing:

#### After the development stage, i performed the following tests

* :hammer: TEST: 
    * Test here..
* :clipboard: RESULT:
    * Results here

[Back to Index](#index)

---

## Testing of Add Person Functionality:

### Initial Testing:

#### After the initial setup of the Add person functionality, i performed the following tests

* :hammer: TEST: 
    * Entered information into all fields in search form, and submitted
* :clipboard: RESULT:
    * A Flash message to inform the user that the person was inserted successfully was displayed.
    * The Mongo collection contained 2 problems:
    * ERRORS: 
	* Where i had not matched the import dictionary with the correct HTML input ID, the type of the document was set to null.
    * FIX: 
	* I matched the import field in the dictionary being imported, to the correct Id in the form.

    * RE-TESTED RESULT: 
	* All fields within each document in MongoDB were inserted correctly.

<br>

* :hammer: TEST:
    * Make sure i could not enter dates manually
* :clipboard: RESULT:
    * No dates can be entered manually.

<br>

* :hammer: TEST:
    * What happens when i try to submit an empty form
* :clipboard: RESULT:   
    * In form validation, using required, ensures that a minimum of somones Umbrella family Circle name, First name, Last name and Date of birth is required.

<br>

* :hammer: TEST:
    * Could i recall all the information from a document
* :clipboard: RESULT: 
    * Using the search feature on the home page, i was able to recall and view any document i entered.

<br>

* :hammer: TEST: 
    * Click submit without filling in the form.
* :clipboard: RESULT:
    * The form did not submit, and an indicator from the HTML Validation displayed to indicate the issue.

*In all cases the pages styling rendered as expected on both mobile, tablet and desktop.*

### Final Testing:

#### After the development stage, i performed the following tests

* :hammer: TEST: 
    * test here..
* :clipboard: RESULT:
    * results here..

[Back to Index](#index)

---

## Testing of edit parents functionality:
Edit Parents, will grab the parents, if they exist, of the person being created/edited, and display them.
It also allows for editing/updating of the parents.

### Initial Testing:

#### After the initial setup of the Add person functionality, i performed the following tests

* :hammer: TEST:  
    * Case where user enters parents name that are new people.
* :clipboard: RESULT:
    * User was able to enter parents details into the blank input form and then click
    **Add Parents** which then took the user to the next stage.  
     On checking MongoDB each document showed the proper linking between the person and the parents, 
     via a parents dictionary within the person. Each parent had a children array containing the personID, which is their child.

<br>

* :hammer: TEST: 
    * Case where user enters parents name that would match an existing person.
* :clipboard: RESULT:
    * The function successfully detected any existing documents within MongoDb that matched the user entry into 
    the form, and so eliminates duplication. The existing documents as well as the person were updated accordingly

<br>

* :hammer: TEST: 
    * Case where user is editing a person that has existing parents.
* :clipboard: RESULT:
    * The function will currently get the existing parents names, and display their details.  
    In the case where they are edited in any way the function will take the data from the form 
    and use them to edit the existing parents data.  
    ***! This is not entirely desirable in all cases***, so to allow for changing of parents to a different parent, 
    a reset parents button would need to be developed and used, to reset any links between existing parents and the person.
    Then return a blank for for editing.

<br>

* :hammer: TEST: 
    * Click submit without filling in the form.
* :clipboard: RESULT:
    * The form did not submit, and an indicator from the HTML Validation displayed to indicate the issue.

*In all cases the pages styling rendered as expected on both mobile, tablet and desktop.*

### Final Testing:

#### After the development stage, i performed the following tests

* :hammer: TEST: 
    * test here..
* :clipboard: RESULT:
    * results here..

[Back to Index](#index)

---

## Testing for Edit Spouse Functionality:
Edit spouse / partner will grab the persons spouse / partners and display them on screen. These partners name are clickable, and for now return you to the same page where you may edit their partners. 
The included form will allow for adding of more partners.

### Initial Testing:

#### After the initial setup of the edit_spouse_partner functionality, i performed the following tests

* :hammer: TEST: 
    * Added a spouse details, and clicked Add Spouse.  
* :clipboard: RESULT:
    * Result was the person was linked to the spouse, but found that the spouse was not linked to the person. Added an update to add the spouse to the person. Re-test showed results as expected.

<br>

* :hammer: TEST: 
    * Click submit without filling in the form.
* :clipboard: RESULT:
    * The form did not submit, and an indicator from the HTML Validation displayed to indicate the issue.   

### After refactor to change spouse / partner to an array:
#### After this development stage, i performed the following tests

* :hammer: TEST: 
    * After refactoring the code to convert the spouse link, to an Array, i performed multiple tests where i created a new person and added a spouse/Partner.
* :clipboard: RESULT:
    * Results in Database were correct and as expected. The results on screen showed the persons spouse / partner list. This list is clickable and clicking on a name, changes the person being edited to the person clicked.

*In all cases the pages styling rendered as expected on both mobile, tablet and desktop.*

### Final Testing:

#### After the development stage, i performed the following tests

* :hammer: TEST: 
    * test here..
* :clipboard: RESULT:
    * results here..

[Back to Index](#index)

---

## Test the Manage Relationship Functionality:
This small function is called if an existing spouse/partner is clicked on to remove it. The function checks to see
if the 2 people have any common children, if they do, then Circles will not allow them to be 'Un-Tied' from eachother. The reason
is that if they have a shared child then they are relevant partners within the structure of someones family Circle
and must remain as partners. The user is taken to a page where they are either allowed to undo the relationship, or informed that they
cannot do that.

### Initial Testing:

#### After the initial setup of the Manage Relationship functionality, i performed the following tests

* :hammer: TEST: 
    * click on a spouse/partner to remove, from within in the edit spouse/ partner page, where the person clicked
    has a common child with the person being edited.
* :clipboard: RESULT:
    * The user is informed that they cannot do this and given the option to return back to the spouse page.   

<br>

* :hammer: TEST: 
    * click on a spouse/partner to remove, from within in the edit spouse/ partner page, where the person clicked
    has no common child with the person being edited.
* :clipboard: RESULT:
    * The user is informed that they can do this and given the option to remove the person as a spouse/partner and also 
    the option to return back to the spouse page.

*In all cases the pages styling rendered as expected on both mobile, tablet and desktop.*
### Final Testing:

#### After the development stage, i performed the following tests

* :hammer: TEST: 
    * test here..
* :clipboard: RESULT:
    * results here..

[Back to Index](#index)

---

## Testing of Edit Siblings Functionality:
The edit siblings page adds someone as the persons sibling, and vice versa.
Also siblings of siblings also become siblings of eachother. As a result, of all this 'heavy lifting', a small delay on form submit is noticable with larger sibling groups.
I am implementing a 'working' indicator for these situations.

### Initial Testing:

#### After the initial setup of the edit_siblings functionality, i performed the following tests

* :hammer: TEST: 
    * Enter a new sibling - (person did not pre-exist in DB) into the form and click Add Sibling.
* :clipboard: RESULT:
    * MongoDB showed sibling correctly added to person array, and the person was added to the sibling within the sibling array.
    Any existing siblings of the person being edited were added to the new sibling as siblings.

<br>

* :hammer: TEST: 
    * Created 2 seperate 2 child families - (Family A and Family B). I then added a new person (Steve) and
    made Steves mother the family A mother, and Steves father the family B father.   
    In the edit siblings page i added a child from family A as a sibling of Steve. And also added one child from family B as
    a sibling of Steve. 
* :clipboard: RESULT:
    * The result was Steve had 4 new siblings, 2 from each family. By adding the one sibling, Circles checked and added the sibling of the sibling
    But due to the parent check within the function the Children in family A did not gain the children of family B as Siblings, 
    and vice versa, Instead they just gained Steve, because Steve had one common parent.

** ***Update : The above test will mostly be redundant as some adding siblings functionality now exists in the 
edit parents function. This was to make the whole building process faster. ie: if i add my father, and he has children, 
then those children can become my siblings.  
However the functionality will remain in place to protect against incorrect siblings of siblings being added***

* :hammer: TEST: 
    * I linked person(A) to 2 siblings. Then linked another person(B) to 2 siblings. I then 
    linked person(A) to person(B) as a sibling.
* :clipboard: RESULT:
    * All person(A)'s siblings became siblings of person(B) and vice versa. also all of their siblings became 
    siblings of eachother, if they had at least one matching parent.

<br>

* :hammer: TEST: 
    * Click submit without filling in the form.
* :clipboard: RESULT:
    * The form did not submit, and an indicator from the HTML Validation displayed to indicate the issue.

*In all cases the pages styling rendered as expected on both mobile, tablet and desktop.*
### Final Testing:

#### After the development stage, i performed the following tests

* :hammer: TEST: 
    * test here..
* :clipboard: RESULT:
    * results here..

[Back to Index](#index)

---

## Testing for check for spouse:
This function checks if the current person being edited has anyone linked as a spouse or a partner. 
If a partner or spouse exists, then the user gets automatically passed on to the edit children page. 
If there is no spouse or partner the user gets passed to a decision page where they can opt to edit 
the person, or return home.

### Initial Testing:

#### After the initial setup of the **your function here** functionality, i performed the following tests

* :hammer: TEST: 
    * Setup a person with no spouse or partner and clicked 'skip to next step' 
    from within the edit siblings page. 
* :clipboard: RESULT:
    * I was taken to a decision page where i clicked edit 'persons name' 
    and i was taken back to the persons edit spouse page, where i could add a spouse/partner. 
    I also repeated this test and clicked on the home link and was taken back to the home screen.
    These results were as expected and correct.  

<br>

* :hammer: TEST: 
    * Setup a person with a spouse or partner and clicked 'skip to next step' 
    from within the edit siblings page. 
* :clipboard: RESULT:
    * I was taken to the edit childrens page which is correct.

### Final Testing:

#### After the development stage, i performed the following tests

* :hammer: TEST: 
    * test here..
* :clipboard: RESULT:
    * results here..

[Back to Index](#index)

---

## Testing of Add Children Functionality:
I have made a change that restricts the user from getting to this page unless the person being edited has a spouse or a partner setup.
The Add children function gets the persons current children and displays them on screen. It also allows the user to 
enter a child to add to the list of persons children. The childs parent selection, and the smart sibling linking means that adding 
one child will update that child with parents and siblings (if present) and vice versa. 

### Initial Testing:

#### After the initial setup of the Add Children functionality, i performed the following tests

* :hammer: TEST: 
    * Add a new child, not in MongoDB as a child of a new person.
* :clipboard: RESULT:
    * Child was updated in both parents documents, in the children array. Also the childs parents field was updated.   

<br>


* :hammer: TEST: 
    * Add a new child, not in MongoDB as a child of a person with 1 existing child. 
* :clipboard: RESULT:
    * Child was updated in both parents documents, in the children array. Also the childs parents field was updated. The siblings field
    of bothe children were updated.

<br>

* :hammer: TEST: 
    * Add a child, that already existed in Mongo DB, that had existing half siblings from another set of parents,
     as a child of a person with 1 existing child. 
* :clipboard: RESULT:
    * Child was updated in both parents documents, in the children array. Also the childs parents field was updated. 
    The sibling fields of any children with a common parent were updated.
### Final Testing:

#### After the development stage, i performed the following tests

* :hammer: TEST: 
    * test here..
* :clipboard: RESULT:
    * results here..

[Back to Index](#index)

---


---
---
---
---
## Template:

### Initial Testing:

#### After the initial setup of the **your function here** functionality, i performed the following tests

* :hammer: TEST: 
    * test here..
* :clipboard: RESULT:
    * results here..

### Final Testing:

#### After the development stage, i performed the following tests

* :hammer: TEST: 
    * test here..
* :clipboard: RESULT:
    * results here..

[Back to Index](#index)

---