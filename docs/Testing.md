
<div align="center">

# Manual ContinuousTesting
All Initial/continuous testing performed between Google Chrome and a Samsung Galaxy S7. Individual browser tests will be performed after the main development stage.

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

**<details><summary>Testing user stories</summary>**

* [Testing user stories](#Testing-user-stories)

</details>

**<details><summary>Code Testing</summary>**

* [Testing of Python Code](#testing-of-python-code)
* [Testing of Javascript Code](#testing-of-javascript)
* [Testing of CSS Code](#testing-of-css)
* [Testing of HTML Code](#HTML-testing)

</details>






---
## Test connection to Heroku.

### Initial Testing:
**<details><summary>After the initial setup of the flask app, and adding the relevant environment variables, and deployment to Heroku I performed the following tests:</summary>**


* :hammer: TEST:    
    * Setup a base route and function and entered a simple return text "This is Circles".
* :clipboard: RESULT: 
    * The result displayed as expected on the local development server.
    * The result displayed as expected on the deployed site via Heroku.

</details>

### Final Testing:

**<details><summary>After the development stage, i performed the following tests:</summary>**

* :hammer: TEST: 
    * After Development stage, checked deployed link on multiple browsers and continued to use the deployed Heroku link
    throughout post-development testing
* :clipboard: RESULT:
    * Website always displayed as expected.
    * No errors in Heroku logs.

</details>

[Back to Index](#index)

---

## Testing of Home page:

### Initial visual tests:

**<details><summary>After initial layout and setup of basic navbar and logo, i performed the following tests</summary>**

* :hammer: TEST: 
    * Viewed Page on various screen sizes to check for overflow and undesired behaviour
* :clipboard: RESULT: 
    * The home page rendered as expected.
    * The responsiveness was good for initial testing.

<br>

* :hammer: TEST: 
    * Clicked the search input
* :clipboard: RESULT:
    * The search input disappeared and the search form appeared. All displayed as expected.

*In all cases the styling of the page rendered as expected on both mobile, tablet and desktop.*

</details>

### Final Testing:

**<details><summary>After the development stage, i performed the following tests</summary>**

* :hammer: TEST: 
    * Checked the home page on multiple browsers and devices
* :clipboard: RESULT:
    * Page rendered as expected.
    * Firefox 79.0 did, however, show some jerky-ness in the glow animation of my logo, and also in the view circles. I have tried 
    Stack overflow and other online resources but as yet have not found a solution for this.

</details>

[Back to Index](#index)

---

## Testing of Search Functionality:
After the initial setup of the search functionality, I decided to move from a single full name search box to a more flexible Mini Form.
I believe provided an experience that was more flexible and desirable, in that I could search by any of First name, last name or DOB, or all together.

### Initial Testing:

**<details><summary>After initial setup - i performed the following tests on the Search functionality</summary>**

I believe provided an experience that was more flexible and desirable, in that I could search by any of First name, last name or DOB, or all together.

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
    * Results for that name and DOB returned from MongoDB as expected.
    * Results were filtered down to reflect the more detailed search.

All results were displayed in a column of clickable results.

### In the case of Errors:

* :hammer: TEST: 
    * Provided a name to the name fields that were not in the Mongo collection.
* :clipboard: RESULT:   
    * The error message passed into the home template from the search function, was successfully displayed in bold.

This did not freeze or break the site and allowed the user to click on the search button, and attempt another search. The message reflected the error.

*In all cases the styling of the page rendered as expected on both mobile, tablet and desktop.*

</details>

### Final Testing:

**<details><summary>After the development stage, i performed the following tests</summary>**

* :hammer: TEST: 
    * Checked the home page/Search feature on multiple browsers and devices
* :clipboard: RESULT:
    *  Search form opens upon clicking the search circles button.
    * I was able to enter any part of a search - first name, last name or date of birth - and get expected results.
    * Trailing Whitespace was ignored on form submission.
    * Entering a name not in the DB, resulted in a message to inform the user of this. 

</details>

[Back to Index](#index)

---

## Testing of Add Person Functionality:
This page allows the user to enter a new person.

### Initial Testing:

**<details><summary>After the initial setup of the Add person functionality, i performed the following tests:</summary>**

* :hammer: TEST: 
    * Entered information into all fields in the search form, and submitted
* :clipboard: RESULT:
    * A Flash message to inform the user that the person was inserted successfully was displayed.
    * The Mongo collection contained 2 problems:
    * ERRORS: 
    * Where I had not matched the import dictionary with the correct HTML input ID, the type of the document was set to null.
    * FIX: 
    * I matched the import field in the dictionary being imported, to the correct id in the form.

    * RE-TESTED RESULT: 
    * All fields within each document in MongoDB were inserted correctly.

<br>

* :hammer: TEST:
    * Make sure I could not enter dates manually
* :clipboard: RESULT:
    * No dates can be entered manually.

<br>

* :hammer: TEST:
    * What happens when I try to submit an empty form
* :clipboard: RESULT:   
    * In-form validation, using required, ensures that a minimum of, First name, Last name and Date of birth is required.

<br>

* :hammer: TEST:
    * Could I recall all the information from a document
* :clipboard: RESULT: 
    * Using the search feature on the home page, I was able to recall and view any document I entered.

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
    * After changing date pickers for Date of Birth to read-only to avoid user input error, tested that form validation still worked
* :clipboard: RESULT:
    * The form submitted without required date of birth, this is not allowed and a script must be added to change this behaviour.

<br>

* :hammer: TEST: 
    * After adding additional form validation to force users to enter the date of birth, into the read-only date of birth input.
* :clipboard: RESULT:
    * The form behaved as expected and required. The form did not submit until the user entered a Date of Birth. The user is guided to do this.

*In all cases the styling of the page rendered as expected on both mobile, tablet and desktop.*

</details>

### Final Testing:

**<details><summary>After the development stage, i performed the following tests:</summary>**

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
    * Upon adding the new person, the editing procedure grabbed the existing person and continued the editing procedure with that existing person.
    * No duplicate person was created.

</details>

[Back to Index](#index)

---

## Testing of Assign parents functionality:
Assign Parents, will grab the parents, if they exist, of the person being created/edited, and display them.

### Initial Testing:

**<details><summary>After the initial setup of the Assign Parents functionality, i performed the following tests:</summary>**

* :hammer: TEST:  
    * Case where the user enters parents name that are new people.
* :clipboard: RESULT:
    * User was able to enter parents details into the blank input form and then click
    **Add Parents** which then took the user to the next stage.  
     On checking MongoDB each document showed the proper linking between the person and the parents, 
     via a parents dictionary within the person. Each parent had a children array containing the personID, which is their child.

<br>

* :hammer: TEST: 
    * Case where the user enters parents name that would match an existing person.
* :clipboard: RESULT:
    * The function successfully detected any existing documents within MongoDB that matched the user entry into the form, and so eliminates duplication. The existing documents, as well as the person, were updated accordingly

<br>

* :hammer: TEST: 
    * Case where the user is editing a person that has existing parents.
* :clipboard: RESULT:
    * The function will currently get the existing parents names and display their details.  
    In the case where they are edited in any way the function will take the data from the form 
    and use them to select the correct parents from the DB, or create new ones.  
    
<br>

* :hammer: TEST: 
    * Click submit without filling in the form.
* :clipboard: RESULT:
    * The form did not submit, and an indicator from the HTML Validation displayed to indicate the issue.

*In all cases the styling of the page rendered as expected on both mobile, tablet and desktop.*

</details>

### Final Testing:

**<details><summary>After the development stage, i performed the following tests:</summary>**

* :hammer: TEST: 
    * Checked the Assign Parents page/form on multiple browsers and devices
* :clipboard: RESULT:
    * Page and form responded perfectly to all browsers.

<br>

* :hammer: TEST: 
    * Performed multiple tests which tested form submission. I left out names and dates in various combinations and attempted to submit.
* :clipboard: RESULT:
    * Form would not submit unless form validation was satisfied.

* :hammer: TEST: 
    * Performed multiple tests where I changed parents to new and/or existing people.
* :clipboard: RESULT:
    * The parent-child relationship was always correct after submission.

<br>

* :hammer: TEST: 
    * Performed multiple tests where I checked the 4 buttons available.
* :clipboard: RESULT:
    * The next button only displayed when parents were already selected, the update, clear and view person buttons as well as the next button, when visible, all
    behaved and worked as expected.

</details>

[Back to Index](#index)

---

## Testing for Assign Spouse or Partner Functionality:
Assign spouse/partner will grab the persons spouse/partners and display them on screen. These partners name are clickable, which leads to a page where they can be removed
so long as they have no shared children. The included form will allow for adding of more partners.

### Initial Testing:

**<details><summary>After the initial setup of the Assign_spouse_partner functionality, i performed the following tests:</summary>**

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

</details>
   

**<details><summary>After refactor to change spouse / partner to an array, i performed the following tests:</summary>**

* :hammer: TEST: 
    * After refactoring the code to convert the spouse link, to an Array, I performed multiple tests where I created a new person and added a spouse/Partner.
* :clipboard: RESULT:
    * Results in Database were correct and as expected. The results on the screen showed the persons spouse/partner list. This list is clickable and clicking on a name, changes the person being edited to the person clicked.

<br>

* :hammer: TEST: 
    * Clicked on existing spouse/partner
* :clipboard: RESULT:
    * Result as expected. was taken to a manage spouse/partner page where, in the case of having no common children, was given the choice to remove the person as a partner, or return to the spouse/partner page.
    * In the case where there were common children, a message explained why I could not remove the partner, and gave me an option to return.

*In all cases the styling of the page rendered as expected on both mobile, tablet and desktop.*

</details>

### Final Testing:

**<details><summary>After the development stage, i performed the following tests:</summary>**

* :hammer: TEST: 
    * Performed multiple tests where i added spouse/partners.
* :clipboard: RESULT:
    * The spouse/partners always added as expected.

<br>

* :hammer: TEST: 
    * Performed multiple tests where I removed spouse/partners.
* :clipboard: RESULT:
    * Circles removed the person and the relationship, where there were no children involved.

<br>

* :hammer: TEST: 
    * Performed multiple tests where I partially completed the forms, leaving out the required information.
* :clipboard: RESULT:
    * The form would not submit unless all required information had been entered.

<br>

* :hammer: TEST: 
    * Performed multiple tests where I checked the 4 buttons available.
* :clipboard: RESULT:
    * All buttons behaved and worked as expected.

</details>

[Back to Index](#index)

---

## Testing of the Manage Relationship Functionality:
This small function is called if an existing spouse/partner is clicked on to remove it. The function checks to see
if the 2 people have any common children, if they do, then Circles will not allow them to be 'Un-Tied' from each other. The reason
is that if they have a shared child then they are relevant partners within the structure of someone's family Circle
and must remain as partners. The user is taken to a page where they are either allowed to undo the relationship, or informed that they
cannot do that.

### Initial Testing:

**<details><summary>After the initial setup of the Manage Relationship functionality, i performed the following tests:</summary>**

* :hammer: TEST: 
    * click on a spouse/partner to remove, from within in the assign spouse/ partner page, where the person clicked
    has a common child with the person being edited.
* :clipboard: RESULT:
    * The user is informed that they cannot do this and given the option to return to the spouse page.   

<br>

* :hammer: TEST: 
    * click on a spouse/partner to remove, from within in the assign spouse/ partner page, where the person clicked
    has no common child with the person being assigned.
* :clipboard: RESULT:
    * The user is informed that they can do this and given the option to remove the person as a spouse/partner and also 
    the option to return to the spouse page.

*In all cases the styling of the page rendered as expected on both mobile, tablet and desktop.*

</details>




### Final Testing:

**<details><summary>After the development stage, i performed the following tests:</summary>**

* :hammer: TEST: 
    * Tested thoughorly in the assign Spouse/partner section
* :clipboard: RESULT:
    * Functionality was all good, worked as expected.

</details>

[Back to Index](#index)

---

## Testing of Assign Siblings Functionality:
The Assign siblings page adds someone as the person's sibling, and vice versa.
Siblings of siblings also become siblings of each other. As a result, of all this 'heavy lifting', a small delay on form submit is noticeable with larger sibling groups.
I am implementing a 'working'/'Please Wait' indicator for these situations.

### Initial Testing:

**<details><summary>After the initial setup of the Assign_siblings functionality, i performed the following tests:</summary>**

* :hammer: TEST: 
    * Enter a new sibling - (the person did not pre-exist in DB) into the form and click Add Sibling.
* :clipboard: RESULT:
    * MongoDB showed sibling correctly added to person array, and the person was added to the sibling within the sibling array.
    Any existing siblings of the person being edited were added to the new sibling as siblings.

<br>

* :hammer: TEST: 
    * Created 2 separate 2 child families - (Family A and Family B). I then added a new person (Steve) and made Steves mother the family A mother, and Steves father the family B father.   
    In the assign siblings page, I added a child from family A as a sibling of Steve. And also added one child from family B as a sibling of Steve. 
* :clipboard: RESULT:
    * The result has Steve had 4 new siblings, 2 from each family. By adding the one sibling, Circles checked and added the sibling of the sibling
    But due to the parent check within the function, the Children in family A did not gain the children of family B as Siblings, 
    and vice versa, Instead they just gained Steve, because Steve had one common parent.

** ***Update: The above test will mostly be redundant as some adding siblings functionality now exists in the assign parents function. This was to make the whole building process faster. ie: if I add my father, and he has children, 
then those children can become my siblings.  
However, the functionality will remain in place to protect against incorrect siblings of siblings being added***

*** ***Update II: Removed the siblings being added at the assign parents stage, as it slowed the assign parents stage noticeably.  my attempts to
reduce the workload, and increase the automated process of adding to a family circle seemed to be skewing the logical flow of the site.
It was slowing the Assign parents functionality just to add all the siblings and as a result, rendered the siblings functionality largely
redundant. 
Sibling functionality should be kept in the Siblings page, so therefore apart from the children section, Assign Siblings is now the only page where you 
can effectively add, or remove siblings***

* :hammer: TEST: 
    * I linked person(A) to 2 siblings. Then linked another person(B) to 2 siblings. I then linked person(A) to person(B) as a sibling.
* :clipboard: RESULT:
    * All person(A)'s siblings became siblings of person(B) and vice versa. also, all of their siblings became siblings of each other, if they had at least one matching parent.

<br>

* :hammer: TEST: 
    * 
* :clipboard: RESULT:
    * The form did not submit, and an indicator from the HTML Validation displayed to indicate the issue.

*In all cases the styling of the page rendered as expected on both mobile, tablet and desktop.*

</details>

### Final Testing:

**<details><summary>After the development stage, i performed the following tests:</summary>**

* :hammer: TEST: 
    * Performed multiple tests where I partially completed the forms, leaving out the required information.
* :clipboard: RESULT:
    * The form would not submit unless all required information had been entered.

<br>

* :hammer: TEST: 
    * Performed multiple tests where I checked the 4 buttons available.
* :clipboard: RESULT:
    * All buttons behaved and worked as expected.

<br>

* :hammer: TEST: 
    * Checked the Assign Siblings feature on multiple browsers and devices
* :clipboard: RESULT:
    * Page rendered as expected
    * I was forced to enter the required information.
    * Trailing Whitespace was ignored on form submission.
    * Entering a name not in the DB, resulted in the creation of new sibling.
    * Entering a name in the DB, resulted in the correct linking of that person, as a child to parents and sibling to other siblings.
<br>

* :hammer: TEST: 
    * Checked the remove Sibling feature in assign children
* :clipboard: RESULT:
    * I was able to remove any child I clicked on.
    * I was returned to assign siblings page correctly.
    * all pages rendered as expected, with the desired amount of information.

</details>

[Back to Index](#index)

---

## Testing of the check for Spouse Functionality:
This function checks if the current person being edited has anyone linked as a spouse or a partner. 
If a partner or spouse exists, then the user gets automatically passed on to the assign children page. 
If there is no spouse or partner the user gets passed to a decision page where they can opt to edit 
the person, or return home.

### Initial Testing:

**<details><summary>After the initial setup of the Check for Spouse functionality, i performed the following tests:</summary>**

* :hammer: TEST: 
    * Setup a person with no spouse or partner and click 'Next' 
    from within the assign siblings page. 
* :clipboard: RESULT:
    * I was taken to a decision page where I clicked edit ' person's name' 
    and I was taken back to the persons assign spouse page, where I could add a spouse/partner. 
    I also repeated this test and clicked on the home link and was taken back to the home screen.
    These results were as expected and correct.  

<br>

* :hammer: TEST: 
    * Setup a person with a spouse or partner and clicked 'Next' 
    from within the assign siblings page. 
* :clipboard: RESULT:
    * I was taken to the assign children's page which is correct.

</details>

### Final Testing:

**<details><summary>After the development stage, i performed the following tests:</summary>**

* :hammer: TEST: 
    * Retested with and without spouse/partners setup.
* :clipboard: RESULT:
    * Results as expected.
    * No spouse or partner, led the user to a page informing them that they cannot add children unless a partner is set.

</details>

[Back to Index](#index)

---

## Testing of Assign Children Functionality:
The Add children function gets the persons current children and displays them on screen. It also allows the user to enter a child to add to the list of the person's children. The child's parent selection, and the smart sibling linking means that adding one child will update that child with parents and siblings (if present) and vice versa. 
I have made a change that restricts the user from getting to this page unless the person being edited has a spouse or a partner setup.

### Initial Testing:

**<details><summary>After the initial setup of the Add Children functionality, i performed the following tests:</summary>**

* :hammer: TEST: 
    * Add a new child, not in MongoDB as a child of a new person.
* :clipboard: RESULT:
    * Child was updated in both parents documents, in the children array. Also, the child's parents field was updated.   

<br>


* :hammer: TEST: 
    * Add a new child, not in MongoDB as a child of a person with 1 existing child. 
* :clipboard: RESULT:
    * Child was updated in both parents documents, in the children array. Also, the child's parents field was updated. The sibling's field of both children was updated.

<br>

* :hammer: TEST: 
    * Add a child, that already existed in Mongo DB, that had existing half-siblings from another set of parents,
     as a child of a person with 1 existing child. 
* :clipboard: RESULT:
    * Child was updated in both parents documents, in the children array. Also, the child's parents field was updated. 
    The sibling fields of any children with a common parent were updated.

</details>

### Final Testing:

**<details><summary>After the development stage, i performed the following tests:</summary>**

* :hammer: TEST: 
    * Performed multiple tests where I partially completed the forms, leaving out the required information.
* :clipboard: RESULT:
    * The form would not submit unless all required information had been entered.

<br>

* :hammer: TEST: 
    * Performed multiple tests where I checked the 4 buttons available.
* :clipboard: RESULT:
    * All buttons behaved and worked as expected.

<br>

* :hammer: TEST: 
    * Checked the Assign Children feature on multiple browsers and devices
* :clipboard: RESULT:
    *  Page rendered as expected
    * I was forced to enter the required information.
    * Trailing Whitespace was ignored on form submission.
    * Entering a name not in the DB, resulted in the creation of a new child.
    * Entering a name in the DB, resulted in incorrect linking of that person, as a child to parents and sibling to other children.
<br>

* :hammer: TEST: 
    * Checked the remove children feature in assign children
* :clipboard: RESULT:
    *  I was able to remove any child I clicked on.
    * I was returned to assign children page correctly.
    * all pages rendered as expected, with the desired amount of information.

</details>

[Back to Index](#index)

---

## Testing of the Manage Child Relationship Functionality:
This small function is called to handle the removal of children. It consists of a landing page for info and calls delete_child to handle the removal. 

### Initial Testing:

**<details><summary>After the initial setup of the Manage Child Relationship functionality, i performed the following tests:</summary>**

* :hammer: TEST: 
    * click on a Child to remove, from within in the assign Children page.
* :clipboard: RESULT:
    * The user is informed and given correct options.
    * Removal handled correctly.   

</details>

### Final Testing:

**<details><summary>After the development stage, i performed the following tests:</summary>**

* :hammer: TEST: 
    * Checked the Remove Children feature on multiple browsers and devices
* :clipboard: RESULT:
    * Page rendered as expected
    * I was given clear information about what I was doing and given correct options.
    * After checking Mongo DB, I found that the removal was handled correctly.

</details>

[Back to Index](#index)

---

## Testing of the Edit Person Relationship Functionality:
This Function is to handle the editing of any person. It is reachable from a link in the view circle page, at the bottom

### Initial Testing:

**<details><summary>After the initial setup of the Edit Person functionality, i performed the following tests:</summary>**

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
    * Check that any changes that conflicted with another person were handled.
* :clipboard: RESULT:
    * If a person was changed in such a way as to be a duplicate of an existing person, Then the user is notified via the notify duplicate functionality.

</details>

### Final Testing:

**<details><summary>After the development stage, i performed the following tests:</summary>**

* :hammer: TEST: 
    * Performed multiple tests where I checked the 4 buttons available.
* :clipboard: RESULT:
    * All buttons behaved and worked as expected.

<br>

* :hammer: TEST: 
    * Checked the Update person feature on multiple browsers and devices
* :clipboard: RESULT:
    *  Page rendered as expected
    * I was able to skip page if no editing was needed.
    * Trailing Whitespace was ignored on form submission.
    * Entering a name not in the DB, resulted in the editing of a current person correctly.
    * Entering a name in the DB, resulted in calling the notify duplicates functionality.

</details>

[Back to Index](#index)

---

## Testing of Notify Duplicates Functionality:
This small function is called to handle the case where editing of a person results in a possible duplicate entry. 

### Initial Testing:

**<details><summary>After the initial setup of the Notify Duplicates functionality, i performed the following tests:</summary>**

* :hammer: TEST: 
    * I edited an existing person to be a duplicate of another existing person.
* :clipboard: RESULT:
    * I was taken to a page where I was correctly informed about the conflict and given a choice to correctly edit the person, 
    or go to the person who was found to be a duplicate.

</details>

### Final Testing:

**<details><summary>After the development stage, i performed the following tests:</summary>**

* :hammer: TEST: 
    * Replicated a duplicate entry on multiple browsers and devices
* :clipboard: RESULT:
    * Handling Page rendered as expected
    * I was able to reverse action and correct/adjust my entry.

</details>

[Back to Index](#index)

---

## Testing of View Circle functionality:

### Initial Testing:

**<details><summary>After the initial setup of the View Circle functionality, i performed the following tests:</summary>**

* :hammer: TEST: 
    * Visual test.
* :clipboard: RESULT:
    * Pages elements rendered as expected

<br>

* :hammer: TEST: 
    * Checked each circle by clicking on them
* :clipboard: RESULT:
    * Each circle redirected me to the correct users circle.

</details>

### Final Testing:

**<details><summary>After the development stage, i performed the following tests:</summary>**

* :hammer: TEST: 
    * Viewed various circles on multiple browsers and devices
* :clipboard: RESULT:
    * Page rendered and behaved as expected.

</details>

[Back to Index](#index)

---

## Testing for Manage people functionality:

### Initial Testing:

**<details><summary>After the initial setup of the Manage People functionality, i performed the following tests:</summary>**

* :hammer: TEST: 
    * Tested searching for a person by the first name
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
    * Entered a new password that didn't match confirm password
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

</details>

### Final Testing:

**<details><summary>After the development stage, i performed the following tests:</summary></summary>**

* :hammer: TEST: 
    * Performed repeat tests as above on multiple browsers
* :clipboard: RESULT:
    * results were as expected and all deletions/removal of relationships were performed cleanly and quickly.

</details>

[Back to Index](#index)

---

# Testing user stories

## The following user stories were identified:

**<details><summary>1.  As a user, I want the home screen to be simple with a clear indication of what I can do.</summary>**

* :hammer: TEST: 
    * Visited the home page.
* :clipboard: RESULT:
    * Found the instruction very simple and clear, and any further information was explained by the use of clear
    breadcrumbs, logical button names and flash messages.

![User story 1 - image 1](https://github.com/Mr-Smyth/circles/blob/master/docs/user-stories/user-story-1-1.png "User Story 1 - image 1")
![User story 1 - image 2](https://github.com/Mr-Smyth/circles/blob/master/docs/user-stories/user-story-1-2.png "User Story 1 - image 2")
![User story 1 - image 3](https://github.com/Mr-Smyth/circles/blob/master/docs/user-stories/user-story-1-3.png "User Story 1 - image 3")
![User story 1 - image 4](https://github.com/Mr-Smyth/circles/blob/master/docs/user-stories/user-story-1-4.png "User Story 1 - image 4")

</details>
 

**<details><summary>2.  As a user, I want to be able to enter my family tree information.</summary>**

* :hammer: TEST: 
    * Visited the Add person page
* :clipboard: RESULT:
    * Was able to enter myself and click add person.
    * Was then guided through a 5 step process that prompted me for all my family circle information.

![User story 2 - image 1](https://github.com/Mr-Smyth/circles/blob/master/docs/user-stories/user-story-2-1.png "User Story 2 - image 1")
![User story 2 - image 2](https://github.com/Mr-Smyth/circles/blob/master/docs/user-stories/user-story-2-2.png "User Story 2 - image 2")
![User story 2 - image 3](https://github.com/Mr-Smyth/circles/blob/master/docs/user-stories/user-story-2-3.png "User Story 2 - image 3")
![User story 2 - image 4](https://github.com/Mr-Smyth/circles/blob/master/docs/user-stories/user-story-2-4.png "User Story 2 - image 4")
![User story 2 - image 5](https://github.com/Mr-Smyth/circles/blob/master/docs/user-stories/user-story-2-5.png "User Story 2 - image 5")


</details>


**<details><summary>3.  As a user, I want a simple way to enter a new person.</summary>**

* :hammer: TEST: 
    * Again visited the add person page.
* :clipboard: RESULT:
    * Easily entered a new person by filling in the add person form.


![User story 3 - image 1](https://github.com/Mr-Smyth/circles/blob/master/docs/user-stories/user-story-3-1.png "User Story 3 - image 1")
![User story 3 - image 2](https://github.com/Mr-Smyth/circles/blob/master/docs/user-stories/user-story-3-2.png "User Story 3 - image 2")


</details>


**<details><summary>4.  As a user, I don't want to have to think about how to connect people in the family circle.</summary>**

* :hammer: TEST: 
    * Visited the Add person page and began to add a family member.
* :clipboard: RESULT:
    * The 5 step process meant I simply had to fill in the blanks on each form.
    * At no stage was I asked any question other than, details of family members.
    * By the end I was able to view my family circle and browse family connections.
    * At no stage did I as a user need to provide any input on the structure.

</details>


**<details><summary>5.  As a user, I want to be able to search my family for a specific person.</summary>**

* :hammer: TEST: 
    * Visited the home page.
* :clipboard: RESULT:
    * After clicking search to reveal the search form, I was able to search for anyone I had entered by any or all of 
    either first name, last name or Date of birth

![User story 5 - image 1](https://github.com/Mr-Smyth/circles/blob/master/docs/user-stories/user-story-5-1.png "User Story 5 - image 1")


</details>


**<details><summary>6.  As a user, I want to be able to see my parental lineage within the database.</summary>**


* :clipboard: RESULT:
    * For this version of Circles, it has not been possible to add this functionality due to time constraints. A future version will have this feature.
    * However a functional view circle page is available by clicking on any search result, and this in turn can be used to trace back through the
    users history.   

![User story 6 - image 1](https://github.com/Mr-Smyth/circles/blob/master/docs/user-stories/user-story-6-1.png "User Story 6 - image 1")


</details>

[Back to Index](#index)

---

# Code Testing

## Testing of Python code:

### app.py:

**<details><summary>app.py Testing</summary>**

* :hammer: TEST: 
    * Checked Gitpods python linter.
* :clipboard: RESULT:
    * The Gitpod editor is clear of all PEP8 errors, except for the env which is not applicable.

<br>

* :hammer: TEST: 
    * Used [pep8online.com](http://pep8online.com)
* :clipboard: RESULT:
    * The online PEP8 check returned 0 errors or warnings

</details>


### utils.py:

**<details><summary>utils.py Testing</summary>**

* :hammer: TEST: 
    * Checked Gitpods python linter.
* :clipboard: RESULT:
    * The Gitpod editor is clear of all PEP8 errors, except for the env which is not applicable.

<br>

* :hammer: TEST: 
    * Used [pep8online.com](http://pep8online.com/checkresult)
* :clipboard: RESULT:
    * The online PEP8 check returned 0 errors or warnings

</details>


### create_update.py:

**<details><summary>create_update.py Testing</summary>**

* :hammer: TEST: 
    * Checked Gitpods python linter.
* :clipboard: RESULT:
    * The Gitpod editor is clear of all PEP8 errors.

<br>

* :hammer: TEST: 
    * Used [pep8online.com](http://pep8online.com/checkresult)
* :clipboard: RESULT:
    * The online PEP8 check returned 0 errors or warnings

</details>

[Back to Index](#index)

<br>

## Testing of Javascript:

### Manage_People.js:

**<details><summary>manage_people.js Testing</summary>**

* :hammer: TEST: 
    * Used JsHint to validate
* :clipboard: RESULT:
    * Js Hint showed no errors.

<br>

* :hammer: TEST: 
    * Checked that the forms in manage people were all opening and closing correctly.
* :clipboard: RESULT:
    * Manage People form elements opened and closed as expected.

<br>

* :hammer: TEST: 
    * Repeated these tests on multiple browsers, and refreshed and hard reset pages multiple times
* :clipboard: RESULT:
    * Manage People form elements opened and closed as expected, and the page displayed as expected with no errors in the console.

</details>

### Home.js:

**<details><summary>home.js Testing</summary>**

* :hammer: TEST: 
    * Used JsHint to validate
* :clipboard: RESULT:
    * Js Hint showed no errors.

<br>

* :hammer: TEST: 
    * Checked that the search form in home page was opening correctly on clicking the search button.
* :clipboard: RESULT:
    * Search form opened as expected.

<br>

* :hammer: TEST: 
    * Repeated this test on multiple browsers, and refreshed and hard reset pages multiple times
* :clipboard: RESULT:
    * Home page search form opened as expected, and the page displayed as expected with no errors in the console.

</details>

### Validate.js:

**<details><summary>validate.js Testing</summary>**

* :hammer: TEST: 
    * Used JsHint to validate
* :clipboard: RESULT:
    * Js Hint showed no errors.

<br>

* :hammer: TEST: 
    * Checked that I could not submit any form without having entered a Date of Birth.
* :clipboard: RESULT:
    * No form anywhere in Circles would allow form submission with a blank Date of Birth.
    * After attempting submission user would be directed to the date of birth input, and in redirected clear text asked to please enter the date of birth.

<br>

* :hammer: TEST: 
    * Checked that I could not submit On Parents page as this is different to a normal single form page.
* :clipboard: RESULT:
    * I could not submit the parents with a blank Date of Birth.
    * After attempting submission user would be directed to the date of birth input, and in placeholder clear text asked to please enter the date of birth.

<br>

* :hammer: TEST: 
    * Checked that page loader activated upon submission.
* :clipboard: RESULT:
    * Page loader loaded after submission.

<br>

* :hammer: TEST: 
    * Repeated these tests on multiple browsers, and refreshed and hard reset pages multiple times
* :clipboard: RESULT:
    * Form pages submitted as expected, and the page displayed as expected with no errors in the console.

</details>

### Utility.js:

**<details><summary>utility.js Testing</summary>**

* :hammer: TEST: 
    * Used JsHint to validate
* :clipboard: RESULT:
    * Js Hint showed no errors.
    * Js Hint showed one warning:
        *   Functions declared within loops referencing an outer scoped variable may lead to confusing semantics. (e, classInvalid)
        * I was unable to achieve a fix on this, the code was taken and credited to Tim in Code Institute.
    * There was 1 undeclared variable.
        * M - this is used for materialize date format.
    * 4 unused variables.
        * These were all materialize related again. Removing them broke my style. So Materialize is dependant on them.
<br>

* :hammer: TEST: 
    * Checked that the materializ dropdown element was showing same validation as the other elements
* :clipboard: RESULT:
    * Form validation displayed as expected.

<br>

* :hammer: TEST: 
    * Checked that all Materialize components behaved as expected.
* :clipboard: RESULT:
    * Yes except for the date picker. If you scroll down the screen to almost halfway mark, before opening the date picker. And
    You then select the year picker, then the top setting for the drop-down seems to be relevant to the page instead of the date picker.
    Checked online and asked on the slack channel. found that it is an issue with materialize, which I will try to fix in Js at a later date, but was not able to 
    fix for this project submission.

<br>


* :hammer: TEST: 
    * Repeated these tests on multiple browsers, and refreshed and hard reset pages multiple times
* :clipboard: RESULT:
    * Form pages behaved as expected, and the page displayed as expected with no errors in the console.


</details>

[Back to Index](#index)

<br>

## Testing of CSS:

## All CSS Files:
All Css files were tested visually on multiple browsers and devices.
Used [W3C CSS Validation](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate.

**<details><summary>base.css Testing</summary>**
Core styling used accross site.

* :hammer: TEST: 
    * Used [W3C CSS Validation](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate add_person.
* :clipboard: RESULT:
    * No Errors shown
    * 54 warnings about unknown user prefixes applied using autoprefixer.   

![Bace.css Validation](https://github.com/Mr-Smyth/circles/blob/master/docs/css-validation/base-css-validation.png "CSS Validation")
    

<br>

* :hammer: TEST: 
    * Tested page on Samsung S7 and S10.
* :clipboard: RESULT:
    * Pages rendered and behaved as expected.

<br>

* :hammer: TEST: 
    * Tested page on Multiple browsers including Chrome, Opera, Firefox and Safari via Browserstack.
* :clipboard: RESULT:
    * Pages rendered and behaved as expected.

</details>


**<details><summary>add_person.css Testing</summary>**

* :hammer: TEST: 
    * Used [W3C CSS Validation](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate add_person.
* :clipboard: RESULT:
    * No Errors shown.
    * 12 warnings about unknown user prefixes applied using autoprefixer.   

![Add Person.css Validation](https://github.com/Mr-Smyth/circles/blob/master/docs/css-validation/add-person-css-validation.png "CSS Validation")

<br>

* :hammer: TEST: 
    * Tested page on Samsung S7 and S10.
* :clipboard: RESULT:
    * Pages rendered and behaved as expected.

<br>

* :hammer: TEST: 
    * Tested page on Multiple browsers including Chrome, Opera, Firefox and Safari via Browserstack.
* :clipboard: RESULT:
    * Pages rendered and behaved as expected.

</details>


**<details><summary>home.css Testing</summary>**
Add on styling for home and manage people pages

* :hammer: TEST: 
    * Used [W3C CSS Validation](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate add_person.
* :clipboard: RESULT:
    * No Errors shown
    * 37 warnings about unknown user prefixes applied using autoprefixer.   

![home.css Validation](https://github.com/Mr-Smyth/circles/blob/master/docs/css-validation/home-css-validation.png "CSS Validation")

<br>

* :hammer: TEST: 
    * Tested page on Samsung S7 and S10.
* :clipboard: RESULT:
    * Pages rendered and behaved as expected.

<br>

* :hammer: TEST: 
    * Tested page on Multiple browsers including Chrome, Opera, Firefox and Safari via Browserstack.
* :clipboard: RESULT:
    * Pages rendered and behaved as expected.

</details>


**<details><summary>view_circle.css Testing</summary>**
Add on styling for home and manage people pages

* :hammer: TEST: 
    * Used [W3C CSS Validation](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate add_person.
* :clipboard: RESULT:
    * No Errors shown
    * 32 warnings about unknown user prefixes applied using autoprefixer.    

![View Circle.css Validation](https://github.com/Mr-Smyth/circles/blob/master/docs/css-validation/view-circle-css-validation.png "CSS Validation")
    

<br>

* :hammer: TEST: 
    * Tested page on Samsung S7 and S10.
* :clipboard: RESULT:
    * Pages rendered and behaved as expected.

<br>

* :hammer: TEST: 
    * Tested page on Multiple browsers including Chrome, Opera, Firefox and Safari via Browserstack.
* :clipboard: RESULT:
    * Pages rendered and behaved as expected.

</details>

[Back to Index](#index)

<br>

# HTML Testing

## All Html files:
All Html files were tested visually and also using a validator. Due to the validator being unable to examine Jinga2 code
I took the code from source. The results are shown here:

**<details><summary>home.html Testing</summary>**
Html Validation

* :hammer: TEST: 
    * Used [W3C HTML Validation](https://validator.w3.org/#validate_by_input) to validate.
* :clipboard: RESULT:
    * No Warnings or errors.
![Home page Validation](https://github.com/Mr-Smyth/circles/blob/master/docs/html-validation/home-html-validation.png "HTML Validation")

</details>

**<details><summary>Assign Children.html Testing</summary>**
Html Validation

* :hammer: TEST: 
    * Used [W3C HTML Validation](https://validator.w3.org/#validate_by_input) to validate.
* :clipboard: RESULT:
    * No Warnings or errors.
![Assign Children page Validation](https://github.com/Mr-Smyth/circles/blob/master/docs/html-validation/assign-children-html-validation.png "HTML Validation")

</details>

**<details><summary>Add Person.html Testing</summary>**
Html Validation

* :hammer: TEST: 
    * Used [W3C HTML Validation](https://validator.w3.org/#validate_by_input) to validate.
* :clipboard: RESULT:
    * No Warnings or errors.
![Add Person page Validation](https://github.com/Mr-Smyth/circles/blob/master/docs/html-validation/add-person-html-validation.png "HTML Validation")

</details>

**<details><summary>Assign Parents.html Testing</summary>**
Html Validation

* :hammer: TEST: 
    * Used [W3C HTML Validation](https://validator.w3.org/#validate_by_input) to validate.
* :clipboard: RESULT:
    * No Warnings or errors.
![Assign parents Validation](https://github.com/Mr-Smyth/circles/blob/master/docs/html-validation/assign-parents-html-validation.png "HTML Validation")

</details>


**<details><summary>Assign Siblings.html Testing</summary>**
Html Validation

* :hammer: TEST: 
    * Used [W3C HTML Validation](https://validator.w3.org/#validate_by_input) to validate.
* :clipboard: RESULT:
    * No Warnings or errors.
![Assign Siblings Validation](https://github.com/Mr-Smyth/circles/blob/master/docs/html-validation/assign-siblings-html-validation.png "HTML Validation")

</details>

**<details><summary>Assign Spouse / Partner.html Testing</summary>**
Html Validation

* :hammer: TEST: 
    * Used [W3C HTML Validation](https://validator.w3.org/#validate_by_input) to validate.
* :clipboard: RESULT:
    * No Warnings or errors.
![Assign Spouse / Partner Validation](https://github.com/Mr-Smyth/circles/blob/master/docs/html-validation/assign-spouse-partner-html-validation.png "HTML Validation")

</details>

**<details><summary>Check if Partner exists.html Testing</summary>**
Html Validation

* :hammer: TEST: 
    * Used [W3C HTML Validation](https://validator.w3.org/#validate_by_input) to validate.
* :clipboard: RESULT:
    * No Warnings or errors.
![Check if Partner exists Validation](https://github.com/Mr-Smyth/circles/blob/master/docs/html-validation/check-if-partner-exists-html-validation.png "HTML Validation")

</details>

**<details><summary>Duplicate Person.html Testing</summary>**
Html Validation

* :hammer: TEST: 
    * Used [W3C HTML Validation](https://validator.w3.org/#validate_by_input) to validate.
* :clipboard: RESULT:
    * No Warnings or errors.
![Duplicate Person.Html Validation](https://github.com/Mr-Smyth/circles/blob/master/docs/html-validation/duplicate-person-html-validation.png "HTML Validation")

</details>

**<details><summary>Edit Person.html Testing</summary>**
Html Validation

* :hammer: TEST: 
    * Used [W3C HTML Validation](https://validator.w3.org/#validate_by_input) to validate.
* :clipboard: RESULT:
    * Showed 1 Error - this was where i am using Jinga if statement to reconstruct the gender dropdown. The multiple
    instance of 'selected' is deliberate and required.
![Edit Person.html Validation](https://github.com/Mr-Smyth/circles/blob/master/docs/html-validation/edit-person-html-validation.png "HTML Validation")

</details>

**<details><summary>Manage Child Relationship.html Testing</summary>**
Html Validation

* :hammer: TEST: 
    * Used [W3C HTML Validation](https://validator.w3.org/#validate_by_input) to validate.
* :clipboard: RESULT:
    * No Warnings or errors.
![Manage Child Relationship.html Validation](https://github.com/Mr-Smyth/circles/blob/master/docs/html-validation/manage-child-relationship-html-validation.png "HTML Validation")

</details>

**<details><summary>Manage Partner Relationship.html Testing</summary>**
Html Validation

* :hammer: TEST: 
    * Used [W3C HTML Validation](https://validator.w3.org/#validate_by_input) to validate.
* :clipboard: RESULT:
    * No Warnings or errors.
![Manage Partner Relationship.html Validation](https://github.com/Mr-Smyth/circles/blob/master/docs/html-validation/manage-partner-relationship-html-validation.png "HTML Validation")

</details>

**<details><summary>Manage People.html Testing</summary>**
Html Validation

* :hammer: TEST: 
    * Used [W3C HTML Validation](https://validator.w3.org/#validate_by_input) to validate.
* :clipboard: RESULT:
    * 2 Errors due to the validator not being able to read the Jinga if statement in the results block.
      The validator thinks there is no closing div, but it is there after the if block.
![Manage People.html Validation](https://github.com/Mr-Smyth/circles/blob/master/docs/html-validation/manage-people-html-validation.png "HTML Validation")

</details>

**<details><summary>Manage Sibling Relationship.html Testing</summary>**
Html Validation

* :hammer: TEST: 
    * Used [W3C HTML Validation](https://validator.w3.org/#validate_by_input) to validate.
* :clipboard: RESULT:
    * No Warnings or errors.
![Manage Sibling Relationship.html Validation](https://github.com/Mr-Smyth/circles/blob/master/docs/html-validation/manage-sibling-relationship-html-validation.png "HTML Validation")

</details>

**<details><summary>View Circle.html Testing</summary>**
Html Validation

* :hammer: TEST: 
    * Used [W3C HTML Validation](https://validator.w3.org/#validate_by_input) to validate.
* :clipboard: RESULT:
    * No Warnings or errors.
![View Circle.html Validation](https://github.com/Mr-Smyth/circles/blob/master/docs/html-validation/view-circle-html-validation.png "HTML Validation")

</details>


[Back to Index](#index)

<br>
