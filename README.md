<div align="center">

# Circles

![Circles logo](https://github.com/Mr-Smyth/circles/blob/master/static/images/circles-logo-400x.png "Site logo")

Circles is a Data Centric, user friendly, Responsive full stack website. 

</div>

Circles enables users to easily create a simple database of their family circles. It will be focused on building 
a family circle around a chosen person, from parents and siblings to spouse and children. While automatically maintaining
the correct relationships involved. This process can then be repeated as often as required for different people.
This will result in a comprehensive data structure of overlapping circles, representing the users family history 
and relationships. Key to this will be that the user will feel that they have had to put no thought into the structure
and layout.  

Users will be able to perform CRUD on the database, via a simple, intuitive front end web page.

This project will be submitted for my Python and Data Centric Development, and third milestone project, in my Full Stack Software Development Diploma. 
The project is a working full-stack site that allows users to manage a
common dataset. It will also demonstrate the technologies I have learned so far.

---
# Index
* [UX](#ux)
    * [Purpose and Goals](#purpose-and-goals)
    * [User Stories](#user-stories)
    * [Opportunities arising from user stories](#opportunities-arising-from-user-stories)

* [UI](#ui)   
    * [Wireframes](#wireframes)   

* [Features](#Features)
    * [Home Page](#Home-Page)
    * [Add Person](#Add-Person-Page)
    * [Edit Parents](#Edit-Parents-Page)
    * [Edit Spouse / Partner](#Edit-Spouse_Partner-Page)
    * [Edit Siblings](#Edit-Siblings-Page)
    * [Edit Children](#Edit-Children-Page)


* [Development](#development)  
    * [Technologies Used](#technologies-used)
    * [Resources Used](#resources-used)
    
     





* [Testing](https://github.com/Mr-Smyth/circles/blob/master/Testing.md)

* [Deploy to Heroku](#deploy-to-heroku)

</div>
---

# UX

## Purpose and Goals

Circles is a web based application, designed to help the user build a family tree - or in this case, Circle!  

There are many Genealogy building websites available today, and many of my friends , as well as myself have tried many of them. And whereas their complexity and effort to cover all 
bases is to be admired, i have found that in that effort lies a flaw for the casual user.   
The problem is, that their must be a tradeoff when building an application that covers every sort of eventuality, the trade is ease of use.  
My experience of friends and family is that from first click, the interface either appears impossibly daunting, or impossible to understand. 
The user is forced into making decisions about how they should structure their data, "Do i start with a person or a family?" 
and left wondering what an event should include, or a citation should be.  

So the goal of this website is to fulfil a simple need for people to know and document their family - Simply. It wont cover every base, and there wont
be fancy graphs - To start with anyway.   
What Circles will provide is simplicity of use, a simple guided building structure built around the model of a family being a circle, comprising
of one person at its hub. The circle will comprise of, Parents, Siblings, Spuse/Partners, and children, all displayed on one page.  
This will also allow a user to click on any of the other people within this circle, to put them at the hub of their own family page. 
Each family circle page, will contain information about the "Hub" person and in this way, will replace all the awkward confusing entries 
requested by more complex family tree builders. It also will allow, once the data has been entered, an interesting journey down the rabbit hole of 
family history and relations.  

For this project version, there will be no user login, anybody who visits the site will be able to begin to add there own family. Future release may include 
'ring-fenced' Circles for each member, but for now i would like to let each circle grow into eachother, and see where it leads. 
Each person is unique in Circles, insofar as the combination of their first and last names combined with the correct date of birth is unique, should this become
a problem, another field could be added to define the uniquness of each person.


This is also complemented by a search feature on the home page allowing you to jump to any person you have created within the database. 
I have chosen this design, as i feel that this is what common people like me want from a genealogy building tool, to keep a track of family connections and information.

[Back to Index](#index)

## User Stories
The Application is intended for users of any age who are deciding on a location for their mini-break, or even just a day out.


The following user stories have been identified:

1.  As a user, I want the home screen to be simple with a clear indication of what i can do. 
2.  As a user, I want to be able to enter my own family tree information.
3.  As a user, I want a simple way to enter a new person.
4.  As a user, I dont want to have to think about how to connect people in the family circle.
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

<br>

# UI 
Simple clean interface is key, the heavy lifting must be done behind the scenes. So i want to keep
the front end completely clutter free. Ideally i am aiming for the user to only need to interact with the search bar, and everything after that
is very intuitive with the correct amount of guidance, and action buttons, with clearly understandable purposes.

I designed the logo first on this application, and found that the logo sat really nicely on a blue background. So the background will be a radial gradient of several similar, subtle shades of blue.
The other colours in use will be shades of indigo and purple for box shading.

I dont want to bamboozle the user with decisions, the person creation procedure takes you through
a defined number of steps, so the user always knows where they are in the process. As a result i need to hard-wire the procedure, and set certain priorities. For
example, Circles does not allow skipping of entering parents in the build process, as parents are something everyone had to have had, to be alive, It is a key piece of information and
aids in the adding of siblings further along. Also it is not possible to advance to step 5 - Assign Siblings, unless you have setup a partner, this is because,
 and i tread carefully here, It is usually required that you have 2 biological parents, 1 of either sex.   
 
 So this is not something the user has to be aware of when starting their circle, It will be either impossible to pass required stages or a notification with a choice
 will be displayed. The focus should be on simply filling in the blanks, answering the questions and circles should do the rest.

After that, i want the search and view to be simple. The user will search for a person, and have clear clickable results showing name and DOB.

The viewing of a persons circle will be interactive and each member of the circle, upon clicking,  will lead the user down a new rabbit hole of discovery.   


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


# Features

Circles will Intelligently guide the user through the Family Circle building process. From a blank Database, the user can click **Add Person** from
the navbar menu. This will take the user to step 1 of 5 optional steps, in building a family circle.
Add Person will provide a form for the user to fill in the details of a new person.   


Clicking Add Person at the foot of the form will add the person to the database and move the user to Step 2, where they can fill in the persons parents details.
This step cannot be skipped unless details have already been entered.   
This is also where Circles begins to help out -   
Circles will grab the parent information and obviously link them as parents of the person being edited, and add the person as a child of the parents.
Both Parents are automatically added as Spouse / partner, as they have a relationship relevant to the family circle.   

Step 3, is about entering a spouse or partners details, this stage can be skipped if not applicable. 
Existing Spouse and partners will be displayed and these links can be clicked on. When clicked on they perform a check to see if they can be removed as a 
spouse or partner, the user will be given the appropriate message and options - If the person being edited, and the spouse/partner clicked on, have 
any existing children, then circles will **NOT** allow the removal of the relationship, as they have a child and therfore are key in the childs circle.
A form allows the user to enter a spouse/partner, again circles will create the new spouse/partner, if they do not already exist. If they do exist, Circles will 
update the relevant relationships.
Having a spouse/partner linked will allow the user to add children to the person at stage 5.

Step 4, is all about entering siblings and again this stage can be skipped if not relevant. 

This is also where Circles manages a lot of the complicated relationships. 
Existing Siblings will be displayed and these links can be clicked on. Clicking on a sibling gives the user the option to remove the sibling, as a sibling.
 When clicked the user will be advised on what they are doing and given the appropriate message and options.
 A form allows the user to enter a Sibling, again circles will create the new Sibling, if they do not already exist, and update parents and possible 
 siblings with this new sibling.  
 If the sibling entered matches an exiting person on the DB, then that person will be selected as a new sibling. Circles will then remove all links, linking the sibling to previous
 parents and siblings, and then begin a process of matching new siblings based on the premise that to be a sibling, in a genealogical way, you must have at 
 least one matching parent. So Circles performs this check on the found sibling, his existing siblings and the siblings of the person being edited. Once 
 that is complete, each sibling will be updated with his or hers own 'Propper' Siblings.


Step 5, is all about entering children and again this stage can be skipped if not relevant.  
This page can only be reached if the person has a spouse / partner.  
Existing Children will be displayed and these links can be clicked on. Clicking on a child gives the user the option to remove the child as a child. 
When clicked the user will be advised on what they are doing and given the appropriate message and options.
A form allows the user to enter a Child, again circles will create the new Child, if they do not already exist, and update parents and possible 
 siblings with this new Child.

If the Child entered matches an exiting person on the DB, then that person will be selected as a new Child.  
Circles will then remove all links, linking the Child to previous parents and siblings, and then begin a process of matching new siblings 
based on the premise that to be a sibling, in a genealogical way, you must have at  least one matching parent. So Circles performs this check on 
the found Child, his existing siblings and the siblings of the person being edited. Once that is complete, each sibling will be updated with his or 
hers own 'Propper' Siblings.   


It is then possible to view this persons circle, and any other circle within.

## Layout

## Home
The Home screen opens with the site logo prominant mid screen. This sits on a circular gradient sky blue background, which 
i choose to best match the site logo. The Logo will glow slightly when hovered over.
There are 3 options in the common Site Navigation, in the top right:

* Home.
* Add Person.
* Manage People.

These are available in a side loading bar in mobile view also.

The search bar which sits under the logo, has a subtle hover effect, and opens into a small search form when clicked.
The search form will search MongoDb, for any or all of the entered data, and return a list of results.

These results are in the form of a large buttoned list, each result shows the full name and the Date of Birth - 
the 2 key pieces of information for finding the person you want. Clicking on any result will take the user to that persons Circle page.

It is paramount that the page is simple, the process has been made simple so the Home page must be a prelude to this.

[Back to Index](#index)
## View Circle
View Circle is reachable from clicking on a search result in the home screen. It is also reachable from a link on each of the edit / Assign pages, within 
the 5 step setup/edit person procedure.   
The view circle page is the goal of the application. It provides a simple view of a persons family circle.   
The page has common site styling with a small logo pushed to the top left of the page, and a common Navigation bar on the top right.
The page heading clearly displays what, and who you are looking at, and immediately below this heading is a profile and information, displaying
details of the person you are viewing, if these details have been entered.   

Below this is each member of the circle, each within a logo-like circle. Hovering over these circles gives a very subtle glow effect, 
similar to the logo on the home page.   

The circles are all arranged with clear headings, displaying the relationship of the person. 
At the bottom of the page is the **Edit (persons Name) Button** which takes the user through the edit process, outlined in the pages below.   

Clicking on any of the Circles, that have names in them takes the user to that persons family circle page, and so on...

You may notice in some cases that instead of a name, you get the option to Assign*, this link will enable you to quickly add a person, So if theperson you are viewing has no siblings, the Assign Sibling button
will be displayed in place of any would be sibling. Clicking the link, will take the user straight to the add sibling page.

Note on above*. This option to Assign will only appear if certain situations arrise. For Example:

* Assign Mother: Will appear if no mother is set - possible in the case where the mother was deleted.   
* Assign Father: Will appear if no father is set - possible in the case where the father was deleted.  
* Assign Spouse / Partner: Will appear if no Spouse / Partner has been set.   
* Assign Sibling: Will appear if no Siblings have been added, and also only if bothe parents have been set.
* Assign Children: Will appear if no children have been added, and also only if the person has a spouse/partner set.   

Any other situations where the user needs to edit, will be covered by clicking the edit button at the bottom of the screen.

This is arranged in such a way to be logical to the user, and maintain a certain logic within Circles itself, 
i.e You cannot have a child who has no parents etc.


[Back to Index](#index)
## Add Person
### Step 1 of 5 
This is selected from the common site navigation bar. 
The page includes common site navigation, and a reduced logo pushed to the top left.
A clear heading, shows the user what page they are on, and clear indication of the stage they are at, in the guided Add Person
process. 
This page includes a detailed form for the user to fill in, to create a person in Circles.  
Clicking on **Add Person**, will Insert the new person, and will automatically take the user to **Step 2 - Assign Parents**.
Clicking **Clear** will reset the form.



[Back to Index](#index)
## Edit Person
### Step 1 of 5 
This is also a Step 1 of 5, it becomes an option to go to this page, when viewing somebodys Circle. It is basically the same layout as Add Person
Except that it is purely for editing existing information of a Person.
This is only selected from the bottom of the view Circles page. 
The page includes common site navigation, and a reduced logo pushed to the top left.
A clear heading, shows the user what page they are on, and clear indication of the stage they are at, in the guided Add Person
process. 
This page includes a detailed form for the user to fill in, to create a person in Circles.  
Clicking on **Update**, will update the person, and will automatically take the user to **Step 2 - Assign Parents**.
Clicking **Clear** will reset the form.
Clicking **Next** will skip to **Step 2 - Assign Parents**.
Clicking **View** (Persons Name) will take the user to the **view Circle page**.




[Back to Index](#index)
## Assign Parents
### Step 2 of 5
This page is reachable from either completing the **Add Person** (Step 1) or **Edit Person** (Step1). It is also possible to reach this page by clicking the 
Assign mother or Assign father buttons in the View Circle page. These buttons are only visable if no mother, or no father is setup.
The page includes common site navigation and a reduced logo pushed to the top left. The persons parents (if already linked in the DB) will be displayed in form. Otherwise
A blank form can be used to enter the persons parents.   
If the Parents are already displayed, then it is still possible to change the parents. However, editing a parent form will not edit the parents details, ***(if you require to
edit a person there is a place for that, which can be accessed from the view circle page)***. Editing or changing the parent form will force Circles to search
for a match, if one is found that person becomes the parent, if no match is found, then a new person is automatically created to become the parent. In this way it 
is not nesseccarry to create each and every person, using the Add person feature, instead they can be added, on the go at each step! 

Important relationship checks, are performed, Person is automatically removed from existing parents as a child, and reassigned to new parents as a child, and 
their parents object is updated accordingly. This is all to ensure, nobody ends up being the son of 2 different mothers.

Clicking on **Add Parents**, will perform the above CRUD, and automatically take the user to **Step 3 - Assign Spouse**.
Clicking **Clear** will reset the form.
Clicking **Next**, is only available, if parents details have been already entered and it will take the user to the next **Step 3 - Assign Spouse**.
Clicking **View** (Persons Name) will take the user to the **view Circle page**.



[Back to Index](#index)

## Assign Spouse_Partner
### Step 3 of 5
This page is reachable by completing the **Assign Parents** page, or by clicking the **Assign Spouse/Partner** link in the **View Circle** page. 
This **Assign Spouse/Partner** button Is only visable in the view circle page, if no spouse / partenr had been setup already.   
The page includes common site navigation and a reduced logo pushed to the top left.
The page will display the Spouse and or Partners of the person being edited, in a row of links, within
a top seperated window.  
Clicking on any of these links will give the option to remove the person as a spouse or partner. However - 
It is not possible to remove someone as a spouse / partner if they have a shared child, 
Circles considers having a child together as a relevant relationship and in this case wont allow the relationship to be
removed.   
To alter a childs parents first search for that child in the home page.   
Next, Select the person and view their circle.
Next, click Edit person at the bottom of the page.
Follow through the steps until you get to Assign Parents, then simply give the person new parents.   

Below this window is a blank form, which will allow the user to add a spouse or partner for the person being edited.
Once added, a new spouse or partner will be immediatly displayed at the top of the page.
Clicking **Add Spouse Partner** will first force Circles to search for a match, if a match is found then that found person
will become a spouse/partner of the person being edited. If no match is found, then the entered information will be used to 
create a new person, who will be a spouse of the person being edited.  
Circles will then return the user to the Edit Spouse Partner page, so more relevant partners may be added.
When the user is finished with this stage, clicking **Next**, will take the user to **Step 4 - Assign Siblings.** 
Clicking **Clear** will reset the form.
Clicking **View** (Persons Name) will take the user to the **view Circle page**.


[Back to Index](#index)
## Assign Siblings
### Step 4 of 5
This page is reachable from completing or skipping the **Assign spouse / partner** page. This page is also reachable by clicking the **Assign Sibling** 
in the view circle page, this button will only be available, if you the person has parents set, and has no existing siblings.
The page includes common site navigation and a reduced logo pushed to the top left.
The page will display any existing Siblings of the person being edited, in a row of links, within
a top seperated window. These links are clickable and when clicked, allow the user to remove the clicked sibling if you choose to.   

Below this window is a blank form, which will allow the user to add a sibling or partner for the person being edited.
Once added, a new spouse or partner will be displayed at the top of the page.
Clicking **Add Sibling** will first force Circles to search for a match. If no match is found, then the entered information will be used to 
create a new person, who will become a Sibling of the person being edited.    

if a match is found then that found person will become a sibling of the person being edited. The found sibling is then removed from all children arrays
in the DB, as they will be reassigned the correct parents from the form, and then added as children of them.   
This approach reduces the risk of duplicating foriegn keys in redundant or non related documents. 
A list of all possible siblings is then gathered including siblings of siblings and siblings of the sibling being added, if 
they had any existing siblings.
A check is then done to add a list of siblings to each sibling, but each sibling that is added must have at least one parent 
in common with the sibling hes being added to.
Unfortunately on larger more complex sibling lists where they span accross half siblings of half siblings, this check can take 
up to 8 - 10 seconds, when adding to sibling lists over 20 in qty. But the user is kept informed that the work is in process.  

Providing this valuable logic, takes a lot of the head breaking work out of adding each sibling individually. So for example, 
with this intelligent approach to adding siblings, adding one sibling will automatically add their 5 other siblings as siblings of you 
and you of them, so long as you have at least one matching parent. 
  
Circles will then return the user to the edit Sibling page, so more Siblings may be added.
When the user is finished with this stage, clicking **Next**, will take the user to **Step 4 Assign Children**, as long as the person has a 
spouse or partner linked.
Clicking **Clear** will reset the form.
Clicking **View** (Persons Name) will take the user to the **view Circle page**.

[Back to Index](#index)
## Assign Children
### Step 5 of 5
This page is reachable from completing or skipping the Assign Sibling page, and only when the person being edited has an existing spouse or partner. 
This page is also reachable, from the view circle page, if the person being viewed has a partner set, and also has no existing children.
The page includes common site navigation and a reduced logo pushed to the top left.
The page will display the existing Children of the person being edited, in a row of links, within
a top seperated window. These links are clickable and when clicked, allow the user to remove the clicked child if you choose to, this will 
also remove the link between the child and the parent being edited. All other links will remain in place

Below this window is a blank form, which will allow the user to add a Child for the person being edited.
Once added, the new child will be displayed at the top of the page.

On clicking Add this child, Circles will search Circles for a match, if none is found, a new person will be created and linked to the selected parents
and to the other children (if any) as siblings.
If a match is found in the DB, fistly that found child will have their id removed from all children arrays, and all sibling arrays in the DB, 
as they will be reassigned the correct parents from the form, and then added as children of them.
All possible siblings will then be collected and checked, then assigned to each propper sibling.
This approach reduces the risk of duplicating foriegn keys in redundant or non related documents.
Circles will then return the user to the edit Sibling page, so more relevant partners may be added.

When the user is finished with this stage, clicking **Done** will return the user to the Home Page.
Clicking **Clear** will reset the form.
Clicking **View** (Persons Name) will take the user to the **view Circle page**.





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

## Resources Used:

*   [Font Awesome](https://fontawesome.com/).
*   [Favicons](https://favicon.io/).
*   [Google Fonts](https://fonts.google.com/).


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
* Setup the **Assign_siblings** route and function.
    * Tested adding siblings and checking relationships.
* Setup the **Assign_Children** route and function.
    * Tested adding Children and checking relationships.
* Setup the **Check_partner exists** route and function.
    * Tested to make sure it detected partners, and allowed access to children.
* Setup the **Manage_partner_relationship** page route and function.
    * Tested removing Spouse / Partners functionality.
* Setup the **Manage_sibling_relationship** page route and function.
    * Tested removing Siblings functionality.
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






# Deploy To Heroku

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
4.  Push file to github.

### Heroku:

#### Create a new application:

1.  Goto the Heroku Dashboard.
2.  Click New.
3.  Select create a new app.
4.  The Heroku app name must be unique, use "–" instead of spaces, and use lower case letters.
5.  Mr-smyth-circles is the name i picked for this application.
6.  Select the region closest – Europe
7.  Click create app.

#### Connecting to the GitHub repository:
There are a number of ways to connect this, or any app. You can use Heroku CLI to connect as 
outlined on the Heroku site. However its simpler to deploy the site from Github, 
that way you only need to push to GitHub.

1.  Select Github, from the Deployment method section, on the Deploy Tab.
2.  Make sure your github id is displayed and then enter the github repository name and click search.
3.  Once it finds the repository, click connect to connect to the repository.

#### Setup the Config Vars.
Attempting to deploy at this stage would result in some unwanted application errors, 
this is because we have hidden our environment variables inside the env file, 
and this is not available to Heroku.

1.  Click on settings.
2.  Click on **Reveal Config Vars**.
3.  This is where we tell heroku what secret variables are required. 
Add the Key Value pairs as follows: **NO QUOTES**
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
Once the Config Vars have been entered you are ready for Automatic Deployment.

1.  Click on the Deploy Tab.
2.  Click enable automatic deploys.
3.  Select the master branch.
4.  Click Deploy branch

#### The Project is now deployed.

[Back to Index](#index)

---
