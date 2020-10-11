<div align="center">

# Circles

![Circles logo](https://github.com/Mr-Smyth/circles/blob/master/static/images/circles-logo-400x.png "Site logo")

Circles is a Data Centric, user friendly full stack website. 

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

Circles is a web based application, designed to help the user build a family tree - or Circle!  

There are many Genealogy building websites available today, and many of my friends , as well as myself have tried many of them. And whereas their complexity and effort to cover all 
bases is to be admired, i have found that in that effort lies a flaw for the casual user.   
The problem is, that their must be a tradeoff when building an application that covers every sort of eventuality, the trade is ease of use.  
My experience of friends and family is that from first click, the interface either appears impossibly daunting, or impossible to understand. 
The user is forced into making decisions about how they should structure their data, "Do i start with a person or a family?" 
and left wondering what an event should include, or a citation should be.  

So the goal of the website is to fulfil a simple need for people to know and document their family - Simply. It wont cover every base, and there wont
be fancy graphs - To start with anyway.   
What Circles will provide is simplicity of use, a simple guided building structure built around the model of a family being a circle, comprising
of one person at its hub. The circle will comprise of, Parents, Siblings, Spuse/key-Partner, and children, all displayed on one page.  
This will also allow a user to click on any of the other people within this circle, to put them at the hub of their own family page. Each family circle page, will contain information about the "Hub" person
and in this way, will replace all the awkward confusing entries requested by more complex family tree builders.

This is also complemented by a search feature on the home page allowing you to jump to any person you have created within the database. 
I have chosen this design, as i feel that this is what common people like me want from a genealogy building tool, to keep a track of family connections and information.

[Back to Index](#index)

## User Stories
The Application is intended for users of any age who are deciding on a location for their mini-break, or even just a day out.


The following user stories have been identified:

1.  As a user, I want the home screen to be simple with a clear indication of what im supposed to do. 
2.  As a user, I want to be able to enter my own family tree information.
3.  As a user, I want a simple way to enter a new person.
4.  As a user, I dont want to have to think about how to connect people in the family circle.
5.  As a user, I want to be able to search my family for a specific person
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
|**See Parental/Maternal Lineage** | 3 | 4 |


</div>

[Back to Index](#index)

<br>

# UI 
Simple clean interface is key, the heavy lifting must be done behind the scenes. So i want to keep
the front end completll clutter free. Ideally i am aiming for the user to only need to interact with the search bar, and everything after that
is very intuitive with the correct amount of guidance, and action buttons, with clearly understandable purposes.

I designed the logo first on this application, and found that the logo sat really nicely on a blue background. So the background will be a radial gradient of several similar, subtle shades of blue.
The other colours in use will be shades of indigo and purple for box shading.

I dont want to bamboozle the user with decisions, the person creation procedure takes you through
a defined number of steps, so the user always knows where they are in the process.

After that, i want the search and view to be simple. The user will search for a person, and have the option to view or edit. A drop down container will also 
be included in the search results, to aid in selecting the correct 'John Smith' for example.

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

## Home Page
The Home screen opens with the site logo prominant mid screen. This sits on a circular gradient sky blue background, which 
i choose to best match the site logo. The search bar which sits under the logo, has a subtle hover effect, and opens into a small search form when clicked.
The search form will search MongoDb, for any or all of the entered data, and return a list of results.

These results are in the form of a collapsible list, each result shows the full name and the Date of Birth - 
the 2 key pieces of information for finding the person you want. When the collapsible is clicked, 
more information relating to that person will be displayed, to give greater clarification, 
and confirm that you are selecting the correct 'John Smith'!  

It is paramount that the page is simple, the process has been made simple so the Home page must be a prelude to this.

[Back to Index](#index)
## Add Person Page
### Step 1 of 5 
This is selected from the menu. 
The page includes common navigation, and a reduced logo pushed to the top left.
A clear heading, shows the user what page they are on, and clear indication of the stage they are at, in the guided Add Person
process. 
This page includes a detailed form for the user to fill in, to create a person in Circles.  
Clicking on Add Person, will perform the above CRUD, and will automatically take the user to step 2 - Edit Parents.
Clicking skip, will take the user to the next step - Edit Spouse.


[Back to Index](#index)
## Edit Parents Page
### Step 2 of 5
This page is reachable from either completing the setup a new person page, or by clicking edit on a search result from the
home page. The page includes common site navigation and a reduced logo pushed to the top left. The persons
parents (if linked in the DB) will be displayed in form,. The form can be edited. 
Editing a parent will first force Circles to remove the persons id from any children field in the DB, this is because if we are 
reassigning parents, the person cannot be a child of someone else.
Circles will then search for a match, if a match is found then that found person will become the parent. The person will then be added as a child of the new parent
and any existing children of the parent will be updated with a new sibling, as will the person also.   

If no match is found, then the entered information will be used to create a new parent. The operations linking new parent to child, and child to parent will all
take place.   

In both cases Circles will ensure that both parents are linked to eachother as partners / spouse as having a child is a relevant 
relationship.    

Clicking on Add Parents, will perform the above CRUD, and automatically take the user to step 3 - Edit Spouse.
Clicking skip, will take the user to the next step - Edit Spouse.

[Back to Index](#index)
## Edit / Add Spouse_Partner Page
### Step 3 of 5
This page is reachable only by completing the Edit Parents page. 
The page includes common site navigation and a reduced logo pushed to the top left.
The page will display the Spouse and or Partners of the person being edited, in a row of links, within
a top seperated window.  
Clicking on any of these links will give the option to remove the person as a spouse or partner. However - 
It is not possible to remove someone as a spouse / partner if they have a shared child, 
Circles considers having a child together as a relevant relationship and in this case wont allow the relationship to be
removed.   
To alter a childs parents search for, and then edit the child in the edit parents page.   

Below this window is a blank form, which will allow the user to add a spouse or partner for the person being edited.
Once added, a new spouse or partner will be immediatly displayed at the top of the page.
Clicking Add Spouse Partner will first force Circles to search for a match, if a match is found then that found person
will become a spouse/partner of the person being edited. If no match is found, then the entered information will be used to 
create a new person, who will be a spouse of the person being edited.  
Circles will then return the user to the Edit Spouse Partner page, so more relevant partners may be added.
When the user is finished with this stage, clicking Skip / Next, will take the user to step 4 - Edit Siblings. 


[Back to Index](#index)
## Edit / Add Siblings Page
### Step 4 of 5
This page is reachable from completing or skipping the edit spouse / partner page. 
The page includes common site navigation and a reduced logo pushed to the top left.
The page will display the Siblings of the person being edited, in a row of links, within
a top seperated window. These links are clickable and when clicked, ****** UPDATE HERE******.   

Below this window is a blank form, which will allow the user to add a sibling or partner for the person being edited.
Once added, a new spouse or partner will be displayed at the top of the page.
Clicking Add Sibling will first force Circles to search for a match. If no match is found, then the entered information will be used to 
create a new person, who will be a spouse of the person being edited.   
if a match is found then that found person will become a sibling of the person being edited. The found sibling is then removed from all children arrays
in the DB, as they will be reassigned the correct parents from the form, and then added as children of them.   
This approach reduces the risk of duplicating foriegn keys in redundant or non related documents. 
A list of all possible siblings is then gathered including siblings of siblings and siblings of the sibling being added, if 
they had any existing siblings.
A check is then done to add a list of siblings to each sibling, but each sibling that is added must have at least one parent 
in common with the sibling hes being added to.
Unfortunately on larger more complex sibling lists where they span accross half siblings of half siblings, this check can take 
10 to 15 seconds in extreme cases. But the user is kept informed that the work is in process.   
Providing this valuable logic, takes a lot of the head breaking work out of adding each sibling individually. So for example, 
with this intelligent approach to adding siblings, adding one sibling will automatically add their 5 other siblings as siblings of you 
and you of them, so long as you have at least one matching parent. 
  
Circles will then return the user to the edit Sibling page, so more relevant partners may be added.
When the user is finished with this stage, clicking Skip / Next, will take the user to step 4, as long as the person has a spouse or partner.

[Back to Index](#index)
## Edit Children Page
### Step 5 of 5
This page is reachable from completing or skipping the edit sibling page, and only when the person being edited has an existing spouse or partner. 
The page includes common site navigation and a reduced logo pushed to the top left.
The page will display the Children of the person being edited, in a row of links, within
a top seperated window. These links are clickable and when clicked, ****** UPDATE HERE******. 

Below this window is a blank form, which will allow the user to add a Child for the person being edited.
Once added, the new child will be displayed at the top of the page.

On clicking Add this child, Circles will search the DB for a match, if none is found, a new person will be created and linked to the selected parents
and to the other children (if any) as siblings.
If a match is found in the DB, fistly that found child will have their id removed from all children arrays
in the DB, as they will be reassigned the correct parents from the form, and then added as children of them.   
This approach reduces the risk of duplicating foriegn keys in redundant or non related documents. The found child is then updated with 
the correct siblings and parents

Circles will then return the user to the edit Sibling page, so more relevant partners may be added.
When the user is finished with this stage, clicking Done will return the user to the persons circle page.


[Back to Index](#index)

---

# Development

## Technologies Used:

*   HTML.
*   CSS.
*   Javascript.
*   Python.
*   Flask micro web framework.
*   Jinga2.
*   MongoDB.
*   GitHub.
*   Heroku.
*   Paint dot net.
*   Balsamiq Wireframes.

## Resources Used:

*   Font Awesome.
*   Favicons.
*   Google Fonts.


## Logic Walkthrough

*   [Planning stages Logic Walkthrough](https://github.com/Mr-Smyth/circles/blob/master/LogicWalkthrough.md)
*   [Planning stages considered Schema](https://github.com/Mr-Smyth/circles/blob/master/Wireframes/database-structure.pdf)

## Development Walkthrough


* Setup a new Database/Collection in MongoDB called Circles.
* Initial setup of resources, libraries, env, gitignore, requirements and folder structure in Flask.
* Setup my Enviroment variables.
* Initial push to Github.
* [Deploy to Heroku](#deploy-to-heroku)
* Setup **Base** and **Home** page template.
    *   This will include the key search feature.
* Setup the **add_person** page, route and function.
* Setup the **edit_parents** page route and function.
* Setup the **edit_spouse** page route and function.
* Setup the **edit_spouse_partner** route and function.




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
