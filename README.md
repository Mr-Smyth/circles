<div align="center">

# Circles

![Circles logo](https://github.com/Mr-Smyth/circles/blob/master/static/images/circles-logo-400x.png "Site logo")


[View the website Deployed using Heroku](https://mr-smyth-circles.herokuapp.com/)


Circles is a Data-Centric, user-friendly, Responsive full-stack website. 

</div>

Circles enable users to easily create a simple database of their family circles. It will be focused on building a family circle around a chosen person, from parents and siblings to spouse and children. While automatically maintaining
the correct relationships involved. This process can then be repeated as often as required for different people.
This will result in a comprehensive data structure of overlapping circles, representing the users family history and relationships. Key to this will be that the user will feel that they have had to put no thought into the structure
and layout.  

Users will be able to perform CRUD on the database, via a simple, intuitive front end web page.

This project will be submitted for my Python and Data-Centric Development, and third milestone project, in my Full Stack Software Development Diploma. 
The project is a working full-stack site that allows users to manage a
common dataset. It will also demonstrate the technologies I have learned so far.

---
# Index

**<details><summary>UX</summary>**

* [UX - General](#ux)
* [Purpose and Goals](#purpose-and-goals)
* [User Stories](#user-stories)
* [Opportunities arising from user stories](#opportunities-arising-from-user-stories)
</details>

**<details><summary>UI</summary>**

* [UI - General](#ui)   
* [Wireframes](#wireframes)
</details>

**<details><summary>Features</summary>**

* [Features - General](#Features)
* [Home Page](#Home)
* [View Circle](#View-circle)
* [Add Person](#Add-Person)
* [Edit Person](#Edit-Person)
* [Assign Parents](#Assign-Parents)
* [Assign Spouse / Partner](#Assign-Spouse_Partner)
* [Assign Siblings](#Assign-Siblings)
* [Assign Children](#Assign-Children)
* [Manage Partner Relationship](#Manage-partner-relationship)
* [Manage Sibling Relationship](#Manage-sibling-relationship)
* [Manage People](#Manage-people)

</details>

**<details><summary>Development</summary>**

* [Development - General](#development)  
* [Technologies Used](#technologies-used)
* [Resources Used](#Resources-used)
* [Pre Project Logic Walkthrough notes](#Logic-Walkthrough)
* [Development Walkthrough](#Development-walkthrough)
* [Problems Encountered during Development](#Problems-Encountered-during-Development)
    
</details>

**<details><summary>Testing</summary>**

* [Testing Documentation](https://github.com/Mr-Smyth/circles/blob/master/docs/Testing.md)
    
</details>

**<details><summary>Deployment</summary>**

* [Deploy to Heroku](#deploy-to-heroku)
* [Local Development](#local-development)
    
</details>

**<details><summary>Credits</summary>**

* [Content and Code](#Content-and-code)
* [Media](#Media)
* [Acknowledgments](#Acknowledgments)
    
</details>

**<details><summary>Disclaimers</summary>**

* [Disclaimer](#Disclaimer)

</details>


</div>

<br>

---

<br>

# UX

## Purpose and Goals

Circles is a web-based application, designed to help the user build a family tree - or in this case, Circle!  

There are many Genealogy building websites available today, and many of my friends, as well as myself, have tried many of them. And whereas their complexity and effort to cover all 
bases are to be admired, I have found that in that effort lies a flaw for the casual user.   
The problem is, that there must be a tradeoff when building an application that covers every sort of eventuality, the trade is the ease of use.  
My experience of friends and family is that from the first click, the interface either appears impossibly daunting, or impossible to understand. 
The user is forced into making decisions about how they should structure their data, "Do I start with a person or a family?" 
and left wondering what an event should include, or a citation should be.  

So the goal of this website is to fulfil a simple need for people to know and document their family - Simply. It won't cover every base, and there won't
be fancy graphs - To start with anyway.   
What Circles will provide is simplicity of use, a simple guided building structure built around the model of a family being a circle, comprising
of one person at its hub. The circle will comprise of, Parents, Siblings, Spouse/Partners, and children, all displayed on one page.  
This will also allow a user to click on any of the other people within this circle, to put them at the hub of their family page. 
Each family circle page will contain information about the "Hub" person and in this way, will replace all the awkward confusing entries requested by more complex family tree builders. It also will allow, once the data has been entered, an interesting journey down the rabbit hole of 
family history and relations.  

For this project version, there will be no user login, anybody who visits the site will be able to begin to add their own family. A future release may include 
'ring-fenced' Circles for each member, but for now I would like to let each circle grow into each other, and see where it leads. 
Each person is unique in Circles, insofar as the combination of their first and last names combined with the correct date of birth is unique, should this become
a problem, another field could be added to define the uniqueness of each person.


This is also complemented by a search feature on the home page allowing you to jump to any person you have created within the database. 
I have chosen this design, as I feel that this is what common people like me want from a genealogy building tool, to keep a track of family connections and information.

[Back to Index](#index)

## User Stories
The Application is intended for users of any age who are deciding on a location for their mini-break, or even just a day out.


The following user stories have been identified:

1.  As a user, I want the home screen to be simple with a clear indication of what I can do. 
2.  As a user, I want to be able to enter my family tree information.
3.  As a user, I want a simple way to enter a new person.
4.  As a user, I don't want to have to think about how to connect people in the family circle.
5.  As a user, I want to be able to search my family for a specific person.
6.  As a user, I want to be able to see my parental lineage within the database.

[Back to Index](#index)

## Opportunities arising from user stories

<div align="center">
 
|Opportunities | Importance | Viability / Feasibility
|-----|:------:|:-----:|
|**Simple Clean Interface** | 5 | 5 |
|**Clearly indicate purpose** | 5 | 5 |
|**Clear Simple Instructions** | 5 | 5 |
|**Simple creation of a new person** | 5 | 5 |
|**Enter Own Family Circle Data** | 5 | 5 |
|**Remove need for user planning of structure**| 5 | 5 |
|**Search Feature** | 5 | 5 |
|**See Parental/Maternal Lineage** | 2 | 3 |


</div>

[Back to Index](#index)

---

<br>

# UI 

![Responsive Image](https://github.com/Mr-Smyth/circles/blob/master/static/images/responsive.png "Responsive-example")

The simple clean interface is key, the heavy lifting must be done behind the scenes. So I want to keep
the front end completely clutter-free. Ideally, I am aiming for the user to only need to interact with the search bar, and everything after that
is very intuitive with the correct amount of guidance, and action buttons, with clearly understandable purposes.

I designed the logo first on this application and found that the logo sat nicely on a blue background. So the background will be a radial gradient of several similar, subtle shades of blue.
The other colours in use will be shades of indigo and purple for box shading.

I don't want to bamboozle the user with decisions, the person creation procedure takes you through
a defined number of steps, so the user always knows where they are in the process. As a result, I need to hard-wire the procedure and set certain priorities. For
example, Circles does not allow skipping of entering parents in the build process, as parents are something everyone had to have had, to be alive, It is a key piece of information and
aids in the adding of siblings further along. Also, it is not possible to advance to step 5 - Assign Siblings, unless you have set up a partner, this is because,
 and I tread carefully here, It is usually required that you have 2 biological parents, 1 of either sex.   
 
 So this is not something the user has to be aware of when starting their circle, It will be either impossible to pass the required stages or a notification with a choice will be displayed. The focus should be on simply filling in the blanks, answering the questions and circles should do the rest.

After that, I want the search and view to be simple. The user will search for a person and have clear clickable results showing name and DOB.

The viewing of a persons circle will be interactive and each member of the circle, upon clicking,  will lead the user down a new rabbit hole of discovery.   

[Back to Index](#index)

## Wireframes

  * [Home Page](https://github.com/Mr-Smyth/circles/blob/master/Wireframes/home-page-wireframe.pdf)


  * [Search Results Page](https://github.com/Mr-Smyth/circles/blob/master/Wireframes/search-results-page-wireframe.pdf)   


  * [New Person Page](https://github.com/Mr-Smyth/circles/blob/master/Wireframes/enter-new-person-page-wireframe.pdf)   


  * [Edit/Add Parents Page](https://github.com/Mr-Smyth/circles/blob/master/Wireframes/edit-parents-page-wireframe.pdf)   


  * [Edit/Add Siblings Page](https://github.com/Mr-Smyth/circles/blob/master/Wireframes/edit-siblings-page-wireframe.pdf)   


  * [Edit/Add Spouse/Partner Page](https://github.com/Mr-Smyth/circles/blob/master/Wireframes/edit-spouse-page-wireframe.pdf)   


  * [Edit/Add Children Page](https://github.com/Mr-Smyth/circles/blob/master/Wireframes/edit-children-page-wireframe.pdf)  


  * [Family Circle Page](https://github.com/Mr-Smyth/circles/blob/master/Wireframes/family-circle-page-wireframe.pdf)   


  [Back to Index](#index)

<br>

# Features

Circles will Intelligently guide the user through the Family Circle building process. From a blank Database, the user can click **Add Person** from
the navbar menu. This will take the user to step 1 of 5 optional steps, in building a family circle.
Add Person will provide a form for the user to fill in the details of a new person.   


Clicking Add Person at the foot of the form will add the person to the database and move the user to Step 2, where they can fill in the persons parents details.
This step cannot be skipped unless details have already been entered.   
This is also where Circles begins to help out -   
Circles will grab the parent information and link them as parents of the person being edited, and add the person as a child of the parents.
Both Parents are automatically added as a Spouse/partner, as they have a relationship relevant to the family circle.   

Step 3, is about entering a spouse or partners details, this stage can be skipped if not applicable. 
Existing Spouse and partners will be displayed and these links can be clicked on. When clicked on they perform a check to see if they can be removed as a 
spouse or partner, the user will be given the appropriate message and options - If the person being edited, and the spouse/partner clicked on, have 
any existing children, then circles will **NOT** allow the removal of the relationship, as they have a child and therefore are key in the child's circle.
A form allows the user to enter a spouse/partner, again circles will create the new spouse/partner if they do not already exist. If they do exist, Circles will 
update the relevant relationships.
Having a spouse/partner linked will allow the user to add children to the person at stage 5.

Step 4, is all about entering siblings and again this stage can be skipped if not relevant. 

This is also where Circles manages a lot of complicated relationships. 
Existing Siblings will be displayed and these links can be clicked on. Clicking on a sibling gives the user the option to remove the sibling, as a sibling.
 When clicked the user will be advised on what they are doing and given the appropriate message and options.
 A form allows the user to enter a Sibling, again circles will create the new Sibling, if they do not already exist, and update parents and possible 
 siblings with this new sibling.  
 If the sibling entered matches an exiting person on the DB, then that person will be selected as a new sibling. Circles will then remove all links, linking the sibling to previous parents and siblings, and then begin a process of matching new siblings based on the premise that to be a sibling, in a genealogical way, you must have at least one matching parent. So Circles performs this check on the found sibling, his existing siblings and the siblings of the person being edited. Once 
 that is complete, each sibling will be updated with his or her own 'Propper' Siblings.


Step 5, is all about entering children and again this stage can be skipped if not relevant.  
This page can only be reached if the person has a spouse/partner.  
Existing Children will be displayed and these links can be clicked on. Clicking on a child gives the user the option to remove the child as a child. 
When clicked the user will be advised on what they are doing and given the appropriate message and options.
A form allows the user to enter a Child, again circles will create the new Child, if they do not already exist, and update parents and possible 
 siblings with this new Child.

If the Child entered matches an exiting person on the DB, then that person will be selected as a new Child.  
Circles will then remove all links, linking the Child to previous parents and siblings, and then begin a process of matching new siblings based on the premise that to be a sibling, in a genealogical way, you must have at least one matching parent. So Circles performs this check on the found Child, his existing siblings and the siblings of the person being edited. Once that is complete, each sibling will be updated with his or 
hers own 'Propper' Siblings.   


It is then possible to view this person circle and any other circle within.

[Back to Index](#index)


## Layout

## Home
The Home screen opens with the site logo prominent mid-screen. This sits on a circular gradient sky blue background, which I choose to best match the site logo. The Logo will glow slightly when hovered over.
There are 3 options in the common Site Navigation, in the top right:

* Home.
* Add Person.
* Manage People.

These are available in a side-loading bar in mobile view also.

The search bar which sits under the logo has a subtle hover effect and opens into a small search form when clicked.
The search form will search MongoDb, for any or all of the entered data, and return a list of results.

These results are in the form of a large buttoned list, each result shows the full name and the Date of Birth - 
the 2 key pieces of information for finding the person you want. Clicking on any result will take the user to that person's Circle page.

The page is completed by site common social media links and copyright information.

It is paramount that the page is simple, the process has been made simple so the Home page must be a prelude to this.

[Back to Index](#index)
## View Circle
View Circle is reachable from clicking on a search result in the home screen. It is also reachable from a link on each of the edit / Assign pages, within the 5 step setup/edit person procedure.   
The view circle page is the goal of the application. It provides a simple view of a person family circle.   
The page has common site styling with a small logo pushed to the top left of the page, and a common navigation bar on the top right.
The page heading displays what, and whom you are looking at, and immediately below this heading is a profile and information, displaying
details of the person you are viewing, if these details have been entered.   

Below this is each member of the circle, each within a logo-like circle. Hovering over these circles gives a very subtle glow effect, 
similar to the logo on the home page.   

The circles are all arranged with clear headings, displaying the relationship of the person. 
At the bottom of the page is the **Edit (person Name) Button** which takes the user through the editing process, outlined in the pages below.   

Clicking on any of the Circles, that have names in them takes the user to that person's family circle page, and so on...

You may notice in some cases that instead of a name, you get the option to Assign*, this link will enable you to quickly add a person, So if the person you are viewing has no siblings, the Assign Sibling button
will be displayed in place of any would-be sibling. Clicking the link will take the user straight to the add sibling page.

Note on above*. This option to Assign will only appear if certain situations arise. For Example:

* Assign Mother: Will appear if no mother is set - possible in the case where the mother was deleted.   
* Assign Father: Will appear if no father is set - possible in the case where the father was deleted.  
* Assign Spouse / Partner: Will appear if no Spouse / Partner has been set.   
* Assign Sibling: Will appear if no Siblings have been added, and also only if both parents have been set.
* Assign Children: Will appear if no children have been added, and also only if the person has a spouse/partner set.   

Any other situations where the user needs to edit will be covered by clicking the edit button at the bottom of the screen.

This is arranged in such a way to be logical to the user, and maintain a certain logic within Circles itself, 
i.e You cannot have a child who has no parents etc.


[Back to Index](#index)
## Add Person
### Step 1 of 5 
This is selected from the common site navigation bar. 
The page includes common site navigation, and a reduced logo pushed to the top left.
A clear heading shows the user what page they are on, and a clear indication of the stage they are at, in the guided Add Person
process. 
This page includes a detailed form for the user to fill in, to create a person in Circles.  
Clicking on **Add Person** will Insert the new person, and will automatically take the user to **Step 2 - Assign Parents**.
If the person added matches an existing person, then no duplicate will be made, the process will continue with the matching existing person.
Clicking **Clear** will reset the form.



[Back to Index](#index)
## Edit Person
### Step 1 of 5 
This is also a Step 1 of 5, it becomes an option to go to this page when viewing somebody's Circle. It is the same layout as Add Person
Except that it is purely for editing existing information of a Person.
This is only selected from the bottom of the view Circles page. 
The page includes common site navigation, and a reduced logo pushed to the top left.
A clear heading shows the user what page they are on, and a clear indication of the stage they are at, in the guided Add Person
process. 
This page includes a detailed form for the user to fill in, it is pre-populated with the data stored in the selected person. The user can edit any of the fields,
But if the user changes info that then matches another person on the DB, then when the user clicks update person, they will be redirected to 
The manage duplicates page, where the user can choose either to return to the person they were editing and change it correctly/differently, 
or they can go to the duplicate person and edit them instead.
In cases where there is no conflict of duplicates, clicking on **Update** will update the person, and will automatically 
take the user to **Step 2 - Assign Parents**.
Clicking **Clear** will reset the form.
Clicking **Next** will skip to **Step 2 - Assign Parents**.
Clicking **View** (Person Name) will take the user to the **view Circle page**.




[Back to Index](#index)
## Assign Parents
### Step 2 of 5
This page is reachable from either completing the **Add Person** (Step 1) or **Edit Person** (Step1). It is also possible to reach this page by clicking the 
**Assign mother** or **Assign father** buttons in the View Circle page. These buttons are only visible if no mother or no father is setup.
The page includes common site navigation and a reduced logo pushed to the top left. The person parents (if already linked in the DB) will be displayed in the form. Otherwise
A blank form can be used to enter the persons parents.   
If Parents are already displayed, then it is still possible to change the parents. However, editing a parent form will not edit the parent's details, ***(if you require to
edit a person there is a place for that, which can be accessed from the view circle page)***. Editing or changing the parent form will force Circles to search
for a match, if one is found that person becomes the parent, if no match is found, then a new person is automatically created to become the parent. In this way it is not necessary to create every person, using the Add person feature, instead, they can be added, on the go at each step! 

Important relationship checks are performed, Person is automatically removed from existing parents as a child, and reassigned to new parents as a child, and their parent's object is updated accordingly. This is all to ensure, nobody ends up being the son of 2 different mothers.

Clicking on **Add Parents** will perform the above CRUD, and automatically take the user to **Step 3 - Assign Spouse**.
Clicking **Clear** will reset the form.
Clicking **Next**, is only available if parents details have been already entered and it will take the user to the next **Step 3 - Assign Spouse**.
Clicking **View** (Person Name) will take the user to the **view Circle page**.



[Back to Index](#index)

## Assign Spouse_Partner
### Step 3 of 5
This page is reachable by completing the **Assign Parents** page, or by clicking the **Assign Spouse/Partner** link in the **View Circle** page. 
This **Assign Spouse/Partner** button Is only visible in the view circle page if no spouse/partner had been setup already.   
The page includes common site navigation and a reduced logo pushed to the top left.
The page will display the Spouse and or Partners of the person being edited, in a row of links, within
a top separated window.  
Clicking on any of these links will give the option to remove the person as a spouse or partner. However - 
It is not possible to remove someone as a spouse/partner if they have a shared child, 
Circles consider having a child together as a relevant relationship and in this case, won't allow the relationship to be
removed.   
To alter a child's parents first search for that child on the home page.   
Next, select the person and view their circle.
Next, click Edit person at the bottom of the page.
Follow through the steps until you get to Assign Parents, then simply give the person new parents.   

Below this window is a blank form, which will allow the user to add a spouse or partner for the person being edited.
Once added, a new spouse or partner will be immediately displayed at the top of the page.
Clicking **Add Spouse Partner** will first force Circles to search for a match, if a match is found then that found person
will become a spouse/partner of the person being edited. If no match is found, then the entered information will be used to create a new person, who will be a spouse of the person being edited.  
Circles will then return the user to the Edit Spouse Partner page, so more relevant partners may be added.
When the user is finished with this stage, clicking **Next**, will take the user to **Step 4 - Assign Siblings.** 
Clicking **Clear** will reset the form.
Clicking **View** (Person Name) will take the user to the **view Circle page**.


[Back to Index](#index)
## Assign Siblings
### Step 4 of 5
This page is reachable from completing or skipping the **Assign spouse/partner** page. This page is also reachable by clicking the **Assign Sibling** 
in the view circle page, this button will only be available, if you the person has parents set, and has no existing siblings.
The page includes common site navigation and a reduced logo pushed to the top left.
The page will display any existing Siblings of the person being edited, in a row of links, within
a top separated window. These links are clickable and when clicked, allow the user to remove the clicked sibling if you choose to.   

Below this window is a blank form, which will allow the user to add a sibling or partner for the person being edited.
Once added, a new spouse or partner will be displayed at the top of the page.
Clicking **Add Sibling** will first force Circles to search for a match. If no match is found, then the entered information will be used to 
create a new person, who will become a Sibling of the person being edited.    

if a match is found then that found person will become a sibling of the person being edited. The found sibling is then removed from all children arrays
in the DB, as they will be reassigned the correct parents from the form, and then added as children of them.   
This approach reduces the risk of duplicating foreign keys in redundant or non-related documents. 
A list of all possible siblings is then gathered including siblings of siblings and siblings of the sibling being added, if 
they had any existing siblings.
A check is then done to add a list of siblings to each sibling, but each sibling that is added must have at least one parent 
in common with the sibling, he's being added to.
Unfortunately, on larger more complex sibling lists where they span across half-siblings of half-siblings, this check can take up to 8 - 10 seconds, when adding to sibling lists over 20 in qty. But the user is kept informed that the work is in process.  

Providing this valuable logic takes a lot of the head breaking work out of adding each sibling individually. So for example, 
with this intelligent approach to adding siblings, adding one sibling will automatically add their 5 other siblings as siblings of you 
and you of them, so long as you have at least one matching parent. 
  
Circles will then return the user to the edit Sibling page, so more Siblings may be added.
When the user is finished with this stage, clicking **Next**, will take the user to **Step 4 Assign Children**, as long as the person has a 
spouse or partner linked.
Clicking **Clear** will reset the form.
Clicking **View** (Person Name) will take the user to the **view Circle page**.

[Back to Index](#index)
## Assign Children
### Step 5 of 5
This page is reachable from completing or skipping the Assign Sibling page, and only when the person being edited has an existing spouse or partner. 
This page is also reachable, from the view circle page, if the person being viewed, has an existing partner already set-up, and also has no existing children.
The page includes common site navigation and a reduced logo pushed to the top left.
The page will display the existing Children of the person being edited, in a row of links, within
a top separated window. These links are clickable and when clicked, allow the user to remove the clicked child if you choose to, this will also remove the link between the child and the parent being edited. All other links will remain in place

Below this window is a blank form, which will allow the user to add a Child for the person being edited.
Once added, the new child will be displayed at the top of the page.

On clicking Add this child, Circles will search Circles for a match, if none is found, a new person will be created and linked to the selected parents
and to the other children (if any) as siblings.
If a match is found in the DB, firstly that found child will have their id removed from all children arrays, and all sibling arrays in the DB, 
as they will be reassigned the correct parents from the form, and then added as children of them.
All possible siblings will then be collected and checked, then assigned to each propper sibling.
This approach reduces the risk of duplicating foreign keys in redundant or non-related documents.
Circles will then return the user to the edit Sibling page, so more relevant partners may be added.

When the user is finished with this stage, clicking **Done** will return the user to the Home Page.
Clicking **Clear** will reset the form.
Clicking **View** (Person Name) will take the user to the **view Circle page**.

[Back to Index](#index)
## Manage Partner Relationship

This page is reachable from the Assign Spouse Partner page, by clicking on any existing Spouse or partner. Once a spouse or partner is clicked, the user is taken to the manage partner relationship page. If the person being edited, and, the selected spouse/partner have no common children, then the user will have 
the option to remove the selected spouse/partner as a spouse/partner.   
Otherwise, the user will get a message informing them that they: "have shared children as a result we cannot separate them as relevant partners". A clear route back to the Assign_spouse Partner page is provided.

[Back to Index](#index)

## Manage Sibling Relationship

This page is reachable from the Assign Sibling page, by clicking on any existing Sibling. Once a Sibling is clicked, the user is taken to the manage sibling relationship page. The user is given information and a clear indication of the importance of what they are about to do.
There are 2 large buttons, one to remove the sibling, as a sibling. The other cancels and returns the user to safety. There is no check here for parents etc,
As the fact they are there means they have at least one common parent, so wanting to remove them could be for any number of reasons that are too numerous to nail down to a background check. So, therefore, any sibling can be removed as a sibling, but the user is also presented with a message explaining that the sibling being removed
Could be added again automatically, and suggests using Manage People as an alternative option.

[Back to Index](#index)


## Manage People

This page is reachable from any page by the Manage People link in the Navigation Menu.
The page opens, with a similar style to the home page, except the logo is pushed to the top left corner. 3 buttons are the main 
the focus of the page **Delete a Person**, **Delete Everyone** and change Password.


*   **Delete a Person** allows you to search for a person by first, last or Date of birth. The user will get a list of results, 
clicking on a link in the results will remove that person and any links to that person in every documents array, object or otherwise in the DB.   

*   **Delete Everyone** gives you the ability to clear everything from the Circles DB. It is password-protected for safety, contact the designer for a password.

*   **Change Password** allows the user to change the delete password, by entering their existing password and entering a new one, then confirm the new password. The user will be notified if the change was successful.


[Back to Index](#index)

---

# Development

## Technologies Used:

*   [HTML](https://github.com/Mr-Smyth/circles/tree/master/templates).
*   [CSS](https://github.com/Mr-Smyth/circles/tree/master/static/css).
*   [Javascript](https://github.com/Mr-Smyth/circles/tree/master/static/js).
*   [Python 3.8.5](https://github.com/Mr-Smyth/circles/blob/master/app.py).
    * [Python 3.8.5 Documentation](https://www.python.org/downloads/release/python-385/)
*   [Flask micro web framework](https://flask.palletsprojects.com/en/1.1.x/).
*   [Jinga2](https://jinja.palletsprojects.com/en/2.11.x/).
*   [MongoDB](https://docs.mongodb.com/).
*   [GitHub](https://github.com/).
*   [Heroku](https://devcenter.heroku.com/categories/reference).
*   [Paint dot net](https://www.getpaint.net/features.html).
*   [Balsamiq Wireframes](https://balsamiq.com/).

[Back to Index](#index)

## Resources Used:

*   [Font Awesome](https://fontawesome.com/).
*   [Favicons](https://favicon.io/).
*   [Google Fonts](https://fonts.google.com/).

[Back to Index](#index)

## Logic Walkthrough

*   [Planning stages Logic Walkthrough](https://github.com/Mr-Smyth/circles/blob/master/docs/LogicWalkthrough.md)
*   [Planning stages considered Schema](https://github.com/Mr-Smyth/circles/blob/master/docs/database-structure.pdf)

## Development Walkthrough

* Setup a new Database/Collection in MongoDB called Circles.
* Initial setup of resources, libraries, env, gitignore, requirements and folder structure in Flask.
* Setup my Enviroment variables.
* Initial push to Github.
* [Deploy to Heroku](#deploy-to-heroku)
* Setup **Base** and **Home** page template.
    *   This will include the key search feature. 
    * Tested deployment and initial setup.
* Setup the **add_person** page, route and function.
    * Tested add person functionality.
* Setup core CSS Styling.
* Setup the **Assign_parents** page route and function.
    * Tested adding and changing parents functionality.
* Setup the **Assign_spouse_Partner** page route and function.
    * Tested adding Spouse / Partners functionality.
* Setup the **Manage_partner_relationship** page route and function.
    * Tested removing Spouse / Partners functionality.
* Setup the **Assign_siblings** route and function.
    * Tested adding siblings and checking relationships.
* Setup the **Manage_sibling_relationship** page route and function.
    * Tested removing Siblings functionality.
* Setup the **Check_partner exists** route and function.
    * Tested to make sure it detected partners, and allowed access to children.
* Setup the **Assign_Children** route and function.
    * Tested adding Children and checking relationships.
* Setup the **Manage_child_relationship** page route and function.
    * Tested removing a child / parent relationship functionality.
* Setup the **Edit_Person** page route and function.
    * Tested Editing a persons details.
* Setup the **Notify_duplicate** page route and function.
    * Tested check for duplication while editing a persons details.
* Setup the **View_Circle** page route and function.
    * Tested Viewing and changing persons functionality.
* Setup the **Manage_People** page route and function.
    * Tested removing People individually and delete all DB functionality.
* Setup error handlers for 404 and 500.
    * Tested these pages.
* Refactored code in **app.py**, to use reusable functions setup within **utils.py** and **create_update.py**.
* Complete CSS Styling.
* Validate code.


[Back to Index](#index)

---
# Problems Encountered during Development:

#### Problem   
My logic on the assign siblings / Parents and Children all involved trying to cut the work of the user. So what I was doing in these views
was at every submit, I was getting every person involved, mostly siblings, checking who each sibling's parents were and comparing them to find
out who is either a full or half-sibling. Then assign them to each sibling/child. It worked great until I quickly realised that the workload went up
exponentially with each new sibling, and after a quick stress test, found that Heroku timed out at around 10 siblings. 

#### Solution   
I knew I still wanted this functionality, so I spread the workload. Any existing siblings were collected with their parents into a nested array
in a fixed format [[child, mother, father],[child, mother, father]] and so on...   
This was all done in the Get portion of the view. The new sibling/child would be then added to this list and within the POST section,
I could easily compare these nested arrays to find out who was who's sibling without multiple database calls pulling the application down as the siblings grew. This worked very well and I added up to 30 siblings without more than a 10-second delay.

#### Problem
A problem relating to the above situation about adding siblings. I needed to let the user know that something was happening when the submit button is clicked. On mobile devices especially where hover effects don't add to visual feedback I felt that I was not sure if I had clicked submit or not.

#### Solution
I added a *"Working ... Please wait"* message and gif. I used Js and CSS to call the loader gif on form submission, 
then cancel it on page load.

#### Problem
I wanted the Date Picker to be Ironclad, in that, I did not want any typed in dates, which was possible if you Tab onto the date picker.
I found that making the date picker read-only only allowed click and select date entry which is exactly what I wanted. However, this led to a bigger
problem, because if you set the date picker input to read-only in HTML, form validation **required** no longer works. So it left the situation
where I could click submit without entering a date of birth. The date of birth is one of the key values I am using to identify people in 
The database and so I had to get a solution.

#### Solution
So I used a JS function to manually check if each date field was not blank if it was I had to also indicate this to the user with an 
inserted red placeholder text, and scroll to the problem input.

#### Problem
The dropdown for the year in the date picker seems to have a top relative to the page after you go down the page so far.
Some js is acting on it because when you get to a certain point, the element style stops applying a top margin.

#### Solution
I was not able to find a solution yet to this problem. It is a problem with materialize, and I have read some attempted botched solutions for it
which I do not like: [Source](https://github.com/Dogfalo/materialize/issues/6388).    
I am considering removing Materialize in a future release, as I have had a poor experience with materialize, and much prefer to either build from
scratch or I may look at another solution such as Materialize Bootstrap, or just Bootstrap.

#### Problem 
Date Pickers for date of birth. Setting them to read-only had also caused the materialize coloured validation to no longer work.

#### Solution
Some rather unstylish, but effective JS code in validate.js. I had a slight problem where on the parent page I was not simply targeting 1 date input, but 2 in the same form.
One for Mother and One for Father. So I started with a check to see what id elements were available. and then got which one was clicked.
I passed the element of the clicked id through and checked if there was an existing date, if so, then give correct colour.   
Then I passed the element through to a function to handle the date picker Modal. As there were 2 DOB's in the parent's form, so there was 2 
Datepickers. I wanted to return to checkColour to set the correct colour, once a selection or clear or cancel was done by the user.
But I need to point at the correct modal, not just the first one in the dom. So I got the parent node of the clicked element and performed
a query on it to find a modal, this gave me the correct modal, and I listened to it for the user click.
Once passed back into checkColour, the correct colour was applied to the date picker, in all circumstances.

#### Footnote
RE: Deletions:   
I was concerned about allowing everyone access and did intend to set up user profiles allowing each profile to setup their circle. But 
Then I realised that there is room for everyone's circle without user logins and that everyone working in the same space could lead to interesting overlaps in circles. I already have over 20 family and friends wanting a copy so they can start adding their own families. So I decided
that instead of user-profiles I would set up a deletion password. I currently only have it requested when you try to delete everyone, but will probably restrict further in the future.

[Back to Index](#index)

---

# Deployment

## Deploy To Heroku

### Setup Requirements:
Make sure Requirements.txt is ***always*** up to date.  
Requirements.txt tells Heroku what resources are needed to run the app.

1.  Goto the Bash Terminal
2.  Type the following: ```pip3 freeze --local > requirements.txt```
3.  Push all changes to GitHub.

### Setup Procfile:
Heroku looks for this Procfile to find out which file runs the app and how to run it.

1.  Goto the Bash Terminal.
2.  Type the following: ```echo web: python app.py > Procfile.```
3.  Open the Procfile, and if there is an empty line, delete it as it can cause problems with Heroku.
4.  Push file to GitHub.

### Heroku:

#### Create a new application:

1.  Goto the Heroku Dashboard.
2.  Click New.
3.  Select to create a new app.
4.  The Heroku app name must be unique, use "–" instead of spaces, and use lower case letters.
5.  Mr-smyth-circles is the name I picked for this application.
6.  Select the region closest – Europe
7.  Click create app.

#### Connecting to the GitHub repository:
There are several ways to connect this or any app. You can use Heroku CLI to connect as outlined on the Heroku site. However its simpler to deploy the site from Github, 
that way you only need to push to GitHub.

1.  Select Github, from the Deployment method section, on the Deploy Tab.
2.  Make sure your GitHub id is displayed and then enter the GitHub repository name and click search.
3.  Once it finds the repository, click connect, to connect to the repository.

#### Setup the Config Vars.
Attempting to deploy at this stage would result in some unwanted application errors, 
this is because we have hidden our environment variables inside the env file, 
and this is not available to Heroku.

1.  Click on settings.
2.  Click on **Reveal Config Vars**.
3.  This is where we tell Heroku what secret variables are required. 
Add the Key-Value pairs as follows: **NO QUOTES**
``` 
    IP : 0.0.0.0   
    PORT: 5000   
    SECRET_KEY: ###########################    
    MONGO_URI : mongodb+srv://root:<MONGO-PASSWORD-HERE>@myfirstcluster.ugdke.mongodb.net/<APP-NAME-HERE>?retryWrites=true&w=majority   
    MONGO_DBNAME: app_name_here  
```
***! Note: You will get this information from the local copy of the env file***   

4.  Click on **Hide Config Vars**.

### Automatic Deployment:
Once the Config Vars has been entered you are ready for Automatic Deployment.

1.  Click on the Deploy Tab.
2.  Click enable automatic deploys.
3.  Select the master branch.
4.  Click Deploy branch

#### The Project is now deployed.

[Back to Index](#index)


## Local Development
To run this project locally on your system - you will need the following components installed on your system:

* Python 3.8 including PIP.
* An IDE for example - VS Code.
* GIT for cloning and version control.
* MongoDB to manage the database either locally or remotely on MongoDB Atlas.

#### Then:
   
1.  Open a Git Bash Command line, in your preferred destination.
2.  Enter git clone and paste in this link `https://github.com/Mr-Smyth/circles.git`
3.  CD into the circle's folder and create a .env file with the correct credentials.
4.  Create a .flaskenv file and add the following entries:
    *   FLASK_APP=run.py
    *   FLASK_ENV=development
5.  Install all requirements from the requirements.txt file. To do this enter:
    *   sudo -H pip3 -r requirements.txt
6.  You should now be able to launch your app locally.
7.  The app should now be running on localhost on an address similar to http://127.0.0.1:5000. Copy/paste this address into your browser.


[Back to Index](#index)

---

<br>

# Credits

## Content and code

*   [MongoDB](https://docs.mongodb.com/) - For excellent documentation.
*   [Code Institute/ Tim Nelson](https://github.com/TravelTimN) - For excellent support and really clear tutorial videos. Thank you so much, you set me on the right path here!
*   [W3 Schools - Python MongoDB](https://www.w3schools.com/python/python_mongodb_getstarted.asp) - invaluable syntax correct help in piecing my
DB calls together.
*   [W3 resource.com](https://www.w3resource.com/mongodb/mongodb-array-update-operator-$push.php) - Helpful code examples.
*   [coders block](https://codersblock.com/blog/creating-glow-effects-with-css/) - Clear instruction on how to implement a glow effect.

[Back to Index](#index)

## Media

*   [Paint dot net](https://www.getpaint.net/features.html) - Used for creating my Logo and circles.
*   [Font Awesome](https://fontawesome.com/) - Used quite a lot in this project, very happy with the outcome.
*   [Favicons](https://favicon.io/) - Solid site icon as usual.

[Back to Index](#index)

## Acknowledgments

*   Big thank you to my Mentor, Aaron - as always a source of good advice and information. Was very quick to accurately point out the possible sticking points in this project, which helped me to plan better and succeed.
*   Thanks again to Tim Nelson, who was invaluable support from the very start of the Data-Centric Module right through to the Project stage. 
*   Thank you to Family members and friends for giving their input on what would interest them in a Geneaology App.

[Back to Index](#index)

---

<br>

# Disclaimer
The content of this Website is for educational purposes only. Users enter data at their own risk.

[Back to Index](#index)

---