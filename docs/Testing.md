
<div align="center">

# Manual ContinuousTesting
All Initial/continuous testing performed between Google Chrome and a Samsung Galaxy S7. Individual browser tests will be performed after main development stage.

[Back to Readme](https://github.com/Mr-Smyth/circles/blob/master/README.md)

---

</div>

# Index

**<details><summary>Heroku</summary>**

* [Test the initial setup connection to Heroku](#test-connection-to-heroku)

</details>

**<details><summary>Individual web page continuous testing</summary>**

* [Testing of Home page](#testing-of-home-page)
* [Testing of Search Functionality](#testing-of-search-functionality)
* [Testing of Add Person Functionality](#testing-of-add-person-functionality)
* [Testing of Assign Parents Functionality](#testing-of-assign-parents-functionality)
* [Testing of Assign Spouse or Partner Functionality](#testing-for-assign-spouse-or-partner-functionality)
* [Testing of Manage Relationship Functionality](#testing-of-the-manage-relationship-functionality)
* [Testing of Assign Sibling Functionality](#testing-of-assign-siblings-functionality)
* [Testing of Check for Spouse Functionality](#testing-of-check-for-spouse-functionality)
* [Testing of Assign Children Functionality](#testing-of-assign-children-functionality)
* [Testing of the Manage Child Relationship Functionality](#Testing-of-the-Manage-Child-Relationship-Functionality)
* [Testing of the Edit Person Relationship Functionality](#Testing-of-the-Edit-Person-Relationship-Functionality)
* [Testing of the Notify Duplicates Functionality](#Testing-of-notify-duplicates-functionality)
* [Testing of View Circle functionality](#Testing-of-View-Circle-functionality)
* [Testing for Manage people functionality](#Testing-for-Manage-people-functionality)
    
</details>


---
## Test connection to Heroku.

### Initial Testing:
**<details><summary>After the initial setup of the flask app, and adding the relevent enviroment variables, and deployment to Heroku i performed the following tests:</summary>**


* :hammer: TEST:	
    * Setup a base route and function and entered a simple return text "This is Circles".
* :clipboard: RESULT: 
    * The result displayed as expected on the local development server.
	* The result displayed as expected on the deployed site via Heroku.

</details>

### Final Testing:

**<details><summary>After the development stage, i performed the following tests:</summary>**

* :hammer: TEST: 
    * After Development stage, checked deployed link on multiple browsers and continued to use the deployed heroku link
    throughout post development testing
* :clipboard: RESULT:
    * Website always displayed as expected.
    * No errors in Heroku logs.

</details>

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
    * Checked the home page on multiple browsers and devices
* :clipboard: RESULT:
    * Page rendered as expected.
    * Firefox 79.0 did however show some jerky-ness in the glow animation of my logo, and also in the view circles. I have tried 
    Stack overflow and other online resources but as yet have not found a solution for this.

[Back to Index](#index)

---

## Testing of Search Functionality:

### Initial Testing:

#### After the initial setup of the search functionality, i decided to move from a single full name search box to a more flexible Mini Form.
I believe provided an experience that was more flexible and desirable, in that i could search by any of First name, last name or DOB, or all together.

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

All results were displayed in a column of clickable results.

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
    * Checked the home page/Search feature on multiple browsers and devices
* :clipboard: RESULT:
    *  Search form opens upon clicking the search circles button.
    * I was able to enter any part of a search - first name, last name or date of birth - and get expected results.
    * Trailing Whitespace was ignored on form submission.
    * Entering a name not in the DB, resulted in a message to inform the user of this. 

[Back to Index](#index)

---

## Testing of Add Person Functionality:
This page allows user to enter a new person.

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
    * In form validation, using required, ensures that a minimum of, First name, Last name and Date of birth is required.

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

<br>

* :hammer: TEST: 
    * After adding a loader gif linked to the submit button - Check that gif was not loading unless validation was satisfied.
* :clipboard: RESULT:
    * The form did not submit, and the gif did not load, unless all validation was true.

<br>

* :hammer: TEST: 
    * After changing date pickers for Date of Birth to readonly to avoid user input error, tested that form validation still worked
* :clipboard: RESULT:
    * The form submitted without required date of birth, this is not allowed and a script must be added to change this behavior.

<br>

* :hammer: TEST: 
    * After adding additional form validation to force users to enter date of birth, into the readonly date of birth input.
* :clipboard: RESULT:
    * The form behaved as expected and required. The form did not submit until the user entered a Date of Birth. The user is guided to do this.

*In all cases the pages styling rendered as expected on both mobile, tablet and desktop.*

### Final Testing:

#### After the development stage, i performed the following tests

* :hammer: TEST: 
    * Checked the Add Person page/form on multiple browsers and devices
* :clipboard: RESULT:
    * Page and form responded perfectly to all browsers.

<br>

* :hammer: TEST: 
    * Checked adding new people, while leaving out first all, then certain required elements one by one.
* :clipboard: RESULT:
    * The form only submitted when all set requirements were met.   

<br>

* :hammer: TEST: 
    * Checked adding a new person who was a duplicate of an existing person.
* :clipboard: RESULT:
    * Upon adding the new person, the edit procedure grabbed the existing person, and continued the edit procedure with that existing person.
    * No duplicate person was created.

[Back to Index](#index)

---

## Testing of Assign parents functionality:
Assign Parents, will grab the parents, if they exist, of the person being created/edited, and display them.

### Initial Testing:

#### After the initial setup of the Assign Parents functionality, i performed the following tests

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
    and use them to select the correct parents from the DB, or create new ones.  
    
<br>

* :hammer: TEST: 
    * Click submit without filling in the form.
* :clipboard: RESULT:
    * The form did not submit, and an indicator from the HTML Validation displayed to indicate the issue.

*In all cases the pages styling rendered as expected on both mobile, tablet and desktop.*

### Final Testing:

#### After the development stage, i performed the following tests

* :hammer: TEST: 
    * Checked the Assign Parents page/form on multiple browsers and devices
* :clipboard: RESULT:
    * Page and form responded perfectly to all browsers.

<br>

* :hammer: TEST: 
    * Performed multiple tests which tested form submission. I left out names and dates in various combinations, and attempted to submit.
* :clipboard: RESULT:
    * Form would not submit unless form validation was satisfied.

* :hammer: TEST: 
    * Performed multiple tests where i changed parents to new and/or existing people.
* :clipboard: RESULT:
    * The parent child relationship was always correct after submission.

<br>

* :hammer: TEST: 
    * Performed multiple tests where i checked the 4 buttons available.
* :clipboard: RESULT:
    * The next button only displayed when parents were already selected, the update, clear and view person buttons as well as the next button, when visable, all
    behaved and worked as expected.

[Back to Index](#index)

---

## Testing for Assign Spouse or Partner Functionality:
Assign spouse / partner will grab the persons spouse / partners and display them on screen. These partners name are clickable, which leads to a page where they can possibly be removed
so long as they have no shared children. The included form will allow for adding of more partners.

### Initial Testing:

#### After the initial setup of the Assign_spouse_partner functionality, i performed the following tests

* :hammer: TEST: 
    * Added a spouse details, and clicked Add Partner.  
* :clipboard: RESULT:
    * Result was the person was linked to the partner, but found that the spouse was not linked to the person. 
    Added an update to add the spouse to the person. Re-test showed results as expected.

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

<br>

* :hammer: TEST: 
    * Clicked on existing spouse/partner
* :clipboard: RESULT:
    * Result as expected. was taken to a manage spouse/partner page where, in the case of having no common children, was given the choice to remove
    the person as a partner, or return back to the spouse/partner page.
    * In the case where there were common children a message explained why i could not remove the partner, and gave me an option to return.

*In all cases the pages styling rendered as expected on both mobile, tablet and desktop.*

### Final Testing:

#### After the development stage, i performed the following tests

* :hammer: TEST: 
    * Performed multiple tests where i added spouse/partners.
* :clipboard: RESULT:
    * The spouse/partners always added as expected.

<br>

* :hammer: TEST: 
    * Performed multiple tests where i removed spouse/partners.
* :clipboard: RESULT:
    * Circles removed the person and the relationship, where there were no children involved.

<br>

* :hammer: TEST: 
    * Performed multiple tests where i partially completed the forms, leaving out required information.
* :clipboard: RESULT:
    * The form would not submit unless all required information had been entered.

<br>

* :hammer: TEST: 
    * Performed multiple tests where i checked the 4 buttons available.
* :clipboard: RESULT:
    * All buttons behaved and worked as expected.

[Back to Index](#index)

---

## Testing of the Manage Relationship Functionality:
This small function is called if an existing spouse/partner is clicked on to remove it. The function checks to see
if the 2 people have any common children, if they do, then Circles will not allow them to be 'Un-Tied' from eachother. The reason
is that if they have a shared child then they are relevant partners within the structure of someones family Circle
and must remain as partners. The user is taken to a page where they are either allowed to undo the relationship, or informed that they
cannot do that.

### Initial Testing:

#### After the initial setup of the Manage Relationship functionality, i performed the following tests

* :hammer: TEST: 
    * click on a spouse/partner to remove, from within in the assign spouse/ partner page, where the person clicked
    has a common child with the person being edited.
* :clipboard: RESULT:
    * The user is informed that they cannot do this and given the option to return back to the spouse page.   

<br>

* :hammer: TEST: 
    * click on a spouse/partner to remove, from within in the assign spouse/ partner page, where the person clicked
    has no common child with the person being assigned.
* :clipboard: RESULT:
    * The user is informed that they can do this and given the option to remove the person as a spouse/partner and also 
    the option to return back to the spouse page.

*In all cases the pages styling rendered as expected on both mobile, tablet and desktop.*
### Final Testing:

#### After the development stage, i performed the following tests

* :hammer: TEST: 
    * Tested thoughorly in the assign Spouse/partner section
* :clipboard: RESULT:
    * Functionality was all good, worked as expected.

[Back to Index](#index)

---

## Testing of Assign Siblings Functionality:
The Assign siblings page adds someone as the persons sibling, and vice versa.
Also siblings of siblings also become siblings of eachother. As a result, of all this 'heavy lifting', a small delay on form submit is noticable with larger sibling groups.
I am implementing a 'working'/'Please Wait' indicator for these situations.

### Initial Testing:

#### After the initial setup of the Assign_siblings functionality, i performed the following tests

* :hammer: TEST: 
    * Enter a new sibling - (person did not pre-exist in DB) into the form and click Add Sibling.
* :clipboard: RESULT:
    * MongoDB showed sibling correctly added to person array, and the person was added to the sibling within the sibling array.
    Any existing siblings of the person being edited were added to the new sibling as siblings.

<br>

* :hammer: TEST: 
    * Created 2 seperate 2 child families - (Family A and Family B). I then added a new person (Steve) and
    made Steves mother the family A mother, and Steves father the family B father.   
    In the assign siblings page i added a child from family A as a sibling of Steve. And also added one child from family B as
    a sibling of Steve. 
* :clipboard: RESULT:
    * The result was Steve had 4 new siblings, 2 from each family. By adding the one sibling, Circles checked and added the sibling of the sibling
    But due to the parent check within the function the Children in family A did not gain the children of family B as Siblings, 
    and vice versa, Instead they just gained Steve, because Steve had one common parent.

** ***Update : The above test will mostly be redundant as some adding siblings functionality now exists in the 
assign parents function. This was to make the whole building process faster. ie: if i add my father, and he has children, 
then those children can become my siblings.  
However the functionality will remain in place to protect against incorrect siblings of siblings being added***

*** ***Update II: Removed the siblings being added at the assign parents stage, as it slowed the assign parents stage noticably.  my attempts to
reduce the workload, and increase the automated process of adding to a family circle seemed to be skewing the logical flow of the site.
It was slowing the Assign parents functionality just to add all the siblings and as a result rendered the siblings functionality largely
redundant. 
Sibling functionality should be kept in the Siblings page, so therefore apart from the children section, Assign Siblings is now the only page where you 
can effectively add, or remove siblings***

* :hammer: TEST: 
    * I linked person(A) to 2 siblings. Then linked another person(B) to 2 siblings. I then 
    linked person(A) to person(B) as a sibling.
* :clipboard: RESULT:
    * All person(A)'s siblings became siblings of person(B) and vice versa. also all of their siblings became 
    siblings of eachother, if they had at least one matching parent.

<br>

* :hammer: TEST: 
    * 
* :clipboard: RESULT:
    * The form did not submit, and an indicator from the HTML Validation displayed to indicate the issue.

*In all cases the pages styling rendered as expected on both mobile, tablet and desktop.*
### Final Testing:

#### After the development stage, i performed the following tests

* :hammer: TEST: 
    * Performed multiple tests where i partially completed the forms, leaving out required information.
* :clipboard: RESULT:
    * The form would not submit unless all required information had been entered.

<br>

* :hammer: TEST: 
    * Performed multiple tests where i checked the 4 buttons available.
* :clipboard: RESULT:
    * All buttons behaved and worked as expected.

<br>

* :hammer: TEST: 
    * Checked the Assign Siblings feature on multiple browsers and devices
* :clipboard: RESULT:
    * Page rendered as expected
    * I was forced to enter the required information.
    * Trailing Whitespace was ignored on form submission.
    * Entering a name not in the DB, resulted in a creation of new sibling.
    * Entering a name in the DB, resulted in correct linking of that person, as child to parents and sibling to other siblings.
<br>

* :hammer: TEST: 
    * Checked the remove Sibling feature in assign children
* :clipboard: RESULT:
    * I was able to remove any child i clicked on.
    * I was returned to assign siblings page correctly.
    * all pages rendered as expected, with desired amount of information.


[Back to Index](#index)

---

## Testing of check for Spouse Functionality:
This function checks if the current person being edited has anyone linked as a spouse or a partner. 
If a partner or spouse exists, then the user gets automatically passed on to the assign children page. 
If there is no spouse or partner the user gets passed to a decision page where they can opt to edit 
the person, or return home.

### Initial Testing:

#### After the initial setup of the Check for Spouse functionality, i performed the following tests

* :hammer: TEST: 
    * Setup a person with no spouse or partner and clicked 'Next' 
    from within the assign siblings page. 
* :clipboard: RESULT:
    * I was taken to a decision page where i clicked edit 'persons name' 
    and i was taken back to the persons assign spouse page, where i could add a spouse/partner. 
    I also repeated this test and clicked on the home link and was taken back to the home screen.
    These results were as expected and correct.  

<br>

* :hammer: TEST: 
    * Setup a person with a spouse or partner and clicked 'Next' 
    from within the assign siblings page. 
* :clipboard: RESULT:
    * I was taken to the assign childrens page which is correct.

### Final Testing:

#### After the development stage, i performed the following tests

* :hammer: TEST: 
    * Restested with and without spouse/partners setup.
* :clipboard: RESULT:
    * Results as expected.
    * No spouse or partner led the user to a page informing them that they cannot add children unless a partner is set.

[Back to Index](#index)

---

## Testing of Assign Children Functionality:
The Add children function gets the persons current children and displays them on screen. It also allows the user to 
enter a child to add to the list of persons children. The childs parent selection, and the smart sibling linking means that adding 
one child will update that child with parents and siblings (if present) and vice versa. 
I have made a change that restricts the user from getting to this page unless the person being edited has a spouse or a partner setup.

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
    * Performed multiple tests where i partially completed the forms, leaving out required information.
* :clipboard: RESULT:
    * The form would not submit unless all required information had been entered.

<br>

* :hammer: TEST: 
    * Performed multiple tests where i checked the 4 buttons available.
* :clipboard: RESULT:
    * All buttons behaved and worked as expected.

<br>

* :hammer: TEST: 
    * Checked the Assign Children feature on multiple browsers and devices
* :clipboard: RESULT:
    *  Page rendered as expected
    * I was forced to enter the required information.
    * Trailing Whitespace was ignored on form submission.
    * Entering a name not in the DB, resulted in a creation of new child.
    * Entering a name in the DB, resulted in correct linking of that person, as child to parents and sibling to other children.
<br>

* :hammer: TEST: 
    * Checked the remove children feature in assign children
* :clipboard: RESULT:
    *  I was able to remove any child i clicked on.
    * I was returned to assign children page correctly.
    * all pages rendered as expected, with desired amount of information.

[Back to Index](#index)

---

## Testing of the Manage Child Relationship Functionality:
This small function is called to handle removal of children. It consists of a landing page for info and calls delete_child to handle the removal. 

### Initial Testing:

#### After the initial setup of the Manage Child Relationship functionality, i performed the following tests

* :hammer: TEST: 
    * click on a Child to remove, from within in the assign Children page.
* :clipboard: RESULT:
    * The user is informed and given correct options.
    * Removal handled correctly.   


### Final Testing:

#### After the development stage, i performed the following tests

* :hammer: TEST: 
    * Checked the Remove Children feature on multiple browsers and devices
* :clipboard: RESULT:
    * Page rendered as expected
    * I was given clear information about what i was doing and given correct options.
    * After checking Mongo DB, i found that, the removal was handled correctly.

[Back to Index](#index)

---

## Testing of the Edit Person Relationship Functionality:
This Function is to handle the editing of any person. It is reachable from a link in the view circle page, at the bottom

### Initial Testing:

#### After the initial setup of the Edit Person functionality, i performed the following tests

* :hammer: TEST: 
    * Check that correct existing information was being populated to the edit form.
* :clipboard: RESULT:
    * All information was displaying correctly

<br>

* :hammer: TEST: 
    * Check that any user changes were updating the DB correctly.
* :clipboard: RESULT:
    * All information was updating correctly.

<br>

* :hammer: TEST: 
    * Check that any changes that conflicted with another person were handled..
* :clipboard: RESULT:
    * If a person was changed in such a way as to be a duplicate of an existing person, Then the user is notified via the notify duplicate functionality.


### Final Testing:

#### After the development stage, i performed the following tests

* :hammer: TEST: 
    * Performed multiple tests where i checked the 4 buttons available.
* :clipboard: RESULT:
    * All buttons behaved and worked as expected.

<br>

* :hammer: TEST: 
    * Checked the Update person feature on multiple browsers and devices
* :clipboard: RESULT:
    *  Page rendered as expected
    * I was able to skip page if no editing was needed.
    * Trailing Whitespace was ignored on form submission.
    * Entering a name not in the DB, resulted in editing of current person correctly.
    * Entering a name in the DB, resulted in calling of the notify duplictaes functionality.

<br>

[Back to Index](#index)

---

## Testing of Notify Duplicates Functionality:
This small function is called to handle the case where editing of a person results in a possible duplicate entry. 

### Initial Testing:

#### After the initial setup of the Notify Duplicates functionality, i performed the following tests

* :hammer: TEST: 
    * I edited an existing person to be a duplicate of another existing person.
* :clipboard: RESULT:
    * I was taken to a page where i was correctly informed about the conflict and given a choice to correctly edit the person, 
    or go to the person who was found to be a duplicate.

### Final Testing:

#### After the development stage, i performed the following tests

* :hammer: TEST: 
    * Replicated a duplicate entry on multiple browsers and devices
* :clipboard: RESULT:
    * Handling Page rendered as expected
    * I was able to reverse action and correct/adjust my entry.
    

[Back to Index](#index)

---

## Testing of View Circle functionality:

### Initial Testing:

#### After the initial setup of the View Circle functionality, i performed the following tests

* :hammer: TEST: 
    * Visual test.
* :clipboard: RESULT:
    * Pages elements rendered as expected

<br>

* :hammer: TEST: 
    * Checked each circle by clicking on them
* :clipboard: RESULT:
    * Each circle redirected me to the correct users circle.

### Final Testing:

#### After the development stage, i performed the following tests

* :hammer: TEST: 
    * Viewed various circles on multiple browsers and devices
* :clipboard: RESULT:
    * Page rendered and behaved as expected.

[Back to Index](#index)

---

## Testing for Manage people functionality:

### Initial Testing:

#### After the initial setup of the Manage People functionality, i performed the following tests

* :hammer: TEST: 
    * Tested searching for a person by first name
* :clipboard: RESULT:
    * Got the correct results.
    * I was able to remove them by clicking on them.

<br>

* :hammer: TEST: 
    * Tested searching for a person by last name
* :clipboard: RESULT:
    * Got the correct results.
    * I was able to remove them by clicking on them.

<br>

* :hammer: TEST: 
    * Tested searching for a person by Date of birth
* :clipboard: RESULT:
    * Got the correct results.
    * was able to remove them by clicking on them.

* :hammer: TEST: 
    * Tested clicking on Delete everyone.
* :clipboard: RESULT:
    * Was asked for the password.
    * When correct password was entered everybody was deleted in the entire DB.
    * When an incorrect or blank password was entered, no deletion took place and the user was notified about the incorrect password entry.

<br>

* :hammer: TEST: 
    * Tested Changing the deletion password.
    * First attempted to change the password by entering an incorrect current password.
* :clipboard: RESULT:
    * General incorrect password message was displayed.
    * Password did not change.

<br>

* :hammer: TEST: 
    * Tested Changing the deletion password.
    * Attempted to change the password by entering the correct current password.
    * Entered a new password that didnt match confirm password
* :clipboard: RESULT:
    * General incorrect password message was displayed.
    * Password did not change.

<br>

* :hammer: TEST: 
    * Tested Changing the deletion password.
    * Attempted to change the password by entering the correct current password.
    * Entered a new password that matched confirm password
* :clipboard: RESULT:
    * Password changed message was displayed.
    * Password changed.

<br>

* :hammer: TEST: 
    * Checked relationships of people who were related to a person removed
* :clipboard: RESULT:
    * No remaining foreign id's existed within any related person.

### Final Testing:

#### After the development stage, i performed the following tests

* :hammer: TEST: 
    * Performed repeat tests as above on multiple browsers
* :clipboard: RESULT:
    * results were as expected and all deletions / removal of relationships were performed cleanly and quickly.

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