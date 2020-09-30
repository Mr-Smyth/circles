<div align="center">

# Circles

![Circles logo](https://github.com/Mr-Smyth/circles/blob/master/static/images/circles-logo-1024x.png "Site logo")

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

* [Development](#development)   
     





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

# Development

## Technologies Used:

## Logic Walkthrough

*   [Planning stages Logic Walkthrough](https://github.com/Mr-Smyth/circles/blob/master/LogicWalkthrough.md)
*   [Planning stages considered Schema](https://github.com/Mr-Smyth/circles/blob/master/Wireframes/database-structure.pdf)

## Development Walkthrough


* Setup a new Database/Collection in MongoDB called Circles.
* Initial setup of resources, libraries, env, gitignore, requirements and folder structure in Flask.
* Setup my Enviroment variables.
* Initial push to Github.
* [Deploy to Heroku](#deploy-to-heroku)
* Setup **Base** and **Home** page templates - this will include the key search feature.
* Setup the **add_person** page, route and function.
* Setup the **edit_parents** page route and function.
* Setup the **edit_spouse** page route and function.




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