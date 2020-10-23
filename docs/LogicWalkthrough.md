# Logic Walkthrough for Circles:

--- 
This is a design stage, crude look through the possible logic required to achieve the goals of the Circles website.
It was necessary to get ideas down on paper - so to speak - and identify the many possible sticking points and difficulties in attempting
to catalogue family connections, in a simple way

Please be aware the code blocks are only to describe my logic process, and aid in my design/build process, and obviously do not represent exact code.

[Back to Readme](https://github.com/Mr-Smyth/circles/blob/master/README.md)

---

## Sample person we will use in this walkthrough:

### Example person's family circle :  
**Name:**  John Doe.  
**Spouse:** Rita Doe (nee Murphy).  
**Father:** Michael Doe.  
**Mother:** Rita Doe (nee Smyth).  
**Siblings:** Mark, Paul, Jane, Helen.  
**Children:** Louie, Stephen, Grace.  

---
<br>

## Possible Data Structure:

Using Mongo DB, the following structure I feel is the best for ease of update and scaling and speed of the query.

* [Data Structure](https://github.com/Mr-Smyth/circles/blob/master/docs/database-structure.pdf)

## Step 1: Register / Login

*   Register to create an account.

<br>

## Step 2: Create a person

* Click on Create/ Edit person.  
This takes the user to a creat person page,
where they enter the following details for John Doe:  

    *  First name
    *  Last name
    *  DOB
    *  DOD
    *  A this is me tick box
    *  General address (not required)
    *  information/Citation: (not required)

* Click submit

#### At this stage the person: A record for John Doe has been created in the People collection in MongoDB

User can be automatically routed to the circle page, with John at its centre. refer to as a hub.

<br>

## Step 3:  Navigation:

* ### Log in

* ### Log out

* ### Register

* ### Home: 
    Will display a Hero image with a centre search bar, inviting the user to search for a person.
    Results should be displayed in a list, and the user can select one.  

    When a user selects a result, they should be routed to the family circle page

    If the user has authority, ***(using front end jinja if loops or python)*** to restrict buttons, an edit button can be clicked.  
    This button will take the user to the edit circle page.


*   ### Circle page (not a clickable link)
    This is a page that will display a selected person, at its hub.  
    Above will be the parents.  
    Below the parents will be siblings.  
    Below the siblings will be the hub person, with a spouse if any.
    Below this will be children if any.

    This represents a query on the DB, as this information will have to be populated via relationships setup.
    An additional query could be included to check lineage of mothers or fathers (ie mother to mother to mother.... or father to father etc)
    This could display a list in order.

* ### Edit circle page:
    This link will actually take the user through multiple pages, this will control the flow of data coming to the database into bitesize chunks.  
    It will also serve to not overwhelm the user, as they will be prompted for people relating to a chosen person, bit by bit.  

    ***The user will arrive here by clicking an Edit link on a person in the search results***


    * **PAGE 1: Edit Parents**:  
    The user will be taken to **edit_parents**, where their parents will be displayed in an editable form if present. Otherwise, a search will be needed to find their parents within the DB.  
    If they are not in DB, they will need to fill out the enter parents form:

        #### FOR FATHER: 
    
        - Give him a first name.  
        - Give him a last name.  
        - give him a DOB.  
        - gender preset to M.  

            
        #### FOR MOTHER :

        - Give her a first name.  
        - Give her a last name.  
        - Give her a maiden name.  
        - give her a DOB.  
        - Gender preset to F.  


        #### WERE PARENTS MARRIED? y/n 
        -  THIS WOULD SET THE SPOUSE FIELD IN BOTH.  
        
        #### CLICKABLE BUTTONS : 
        * Next - saves changes to DB and moves to siblings page
        * Skip - Moves to siblings page

        ### LOGIC WALKTHROUGH FOR PARENTS:


            CHECK IF JOHN HAS PARENTS
            IF THEY ARE IN DB, DISPLAY THEM IN FORM

            # SETUP A SEARCH

            # SETUP AN ARRAY OF DICTS' CALLED PARENTS, TO IMPORT THE PARENTS
            PARENTS = [
            
                # INSERT FATHER
                {
                FIRST_NAME: FORM FATHERS_FIRST_NAME
                LAST_NAME: FORM FATHERS_LAST_NAME
                DOB: FORM FATHERS_DOB
                DOD: FORM FATHERS_DOD
                GENDER: MALE
                CHILDREN : [ LIST_OF_CHILDREN]
                },
                # INSERT MOTHER
                {
                FIRST_NAME: FORM MOTHERS_FIRST_NAME
                LAST_NAME: FORM MOTHERS_LAST_NAME
                MAIDEN_NAME: FORM MOTHERS_MAIDEN_NAME
                DOB: FORM MOTHERS_DOB
                DOD: FORM MOTHERS_DOD
                GENDER: FEMALE
                CHILDREN: [ LIST_OF_CHILDREN]
                },

            ]
            
            INSERT MANY(PARENTS)
            THIS RETURNS THE IDS IN A LIST OF THE INSERTED DOCUMENTS

            SAVE THIS INTO A VARIABLE CALLED FATHER_MOTHER_IDS

            SO THE FIRST ID IN THE LIST IS THE FATHERS ID AND IF PARENTS WERE MARRIED, THIS ID MUST BE INSERTED TO 
                THE MOTHER, IN THE SPOUSE FIELD. 
            THE SECOND ID IN THE LIST IS THE ID OF THE MOTHER, IF PARENTS WERE MARRIED, THIS ID MUST BE INSERTED TO
                THE FATHER IN THE SPOUSE FIELD
            INSERT ID OF FATHER AND MOTHER INTO JOHN RECORD

            # SO AT THIS POINT JOHN HAS A LINK TO HIS PARENTS
                AND IF MARRIED, THE PARENTS ARE LINKED IN THEIR INDIVIDUAL SPOUSE FIELDS



    ---
    ---


    * **PAGE 2: Edit Siblings**:  
    The user will be taken to **edit_siblings**, where their siblings will be displayed in an editable form if present. Otherwise, a search will be needed to find their parents within the DB.  
    If they are not in DB, they will need to fill out the enter siblings form:

        * Give her/him a first name. 
        * Give her/him a last name.   
        * Maiden name:   
        * give her/him a DOB:   
        * Select gender:   

        ( DYNAMICALLY ADD ANOTHER SIBLING INPUT - CLICK +SIBLING? ).   
        ( POSSIBLE CHECK NEEDED - WHEN ENTERING A NAME AND DOB, - CHECK Name & DOB PAIR FOR REPEAT ENTRY?

        #### CLICKABLE BUTTONS : 
        * Next - saves changes to DB and moves to Spouse page
        * Skip - Moves to spouse page



        #### LOGIC WALKTHROUGH FOR SIBLINGS:
        
            # SETUP A SIBLING SEARCH FOR JOHN AND DISPLAY IF ANY RESULTS

            # I WILL NOT KNOW HOW MANY SIBLINGS THERE ARE AS HOPING TO ADD INPUTS DYNAMICALLY FOR SIBLINGS (USING JS) AS REQUIRED
            # SO DO A LOOP? 

            FOR I IN RANGE OF 0 TO 50
                IF INPUT FROM FORM SIBLING[ i ] EXISTS
                    CREATE SIBLING IN A DICTIONARY
                    ADD DICTIONARY TO A LIST_OF_SIBLINGS - WHICH IS A LIST OF DICTIONARIES

            # END RESULT HERE SHOULD HAVE A LIST DICTIONARIES CONTAINING ALL SIBLINGS
            
            INSERT THE LIST_OF_SIBLINGS INTO MongoDB

            THIS RETURNS A LIST OF THE IDS
            ADD JOHNS ID TO THIS LIST.


            # UPDATE THE PARENTS
                BUILD A LIST CALLED ALL_SIBLINGS_IDS
                    
                ADD THE ALL_SIBLINGS_IDS TO EACH PARENT INTO THE FIELD CHILDREN:

            # GET THE ID OF BOTH PARENTS
                WE CAN GET THIS FROM JOHN WHO HAS LINK TO PARENTS FROM PARENT ENTRY STAGE
            
            # UPDATE EACH SIBLING:

            ALL_SIBLING_ID = [ 10001, 10002, 10003, 10004 ]

            CREATE A LIST OF IDS FOR EACH ID - MEANING A LIST FOR ID 10001, MUST NOT CONTAIN 10001. ETC
                ADD THIS LIST TO THE CORRECT SIBLING
                ADD MOTHER ID TO MOTHER WITHIN EACH SIBLING
                ADD FATHERS ID TO FATHER WITHIN EACH SIBLING

            # THAT SHOULD GET US TO THE STAGE WHERE WE HAVE A LIST OF SIBLING ID'S
                LINKED TO EVERY SIBLING, BUT THE LIST DOES NOT INCLUDE THEMSELVES.
            # A LIST OF CHILDREN ID'S SHOULD ALSO BE IN EACH PARENT.
            # THE SIBLINGS HAVE THEIR PARENTS IDS

        

    ---
    ---

    * **PAGE 3: Edit SPOUSE**:  
    The user will be taken to **edit_spouse**, where their spouse will be displayed in an editable form if present. Otherwise, a search will be needed to find their parents within the DB.  
    If they are not in DB, they will need to fill out the enter spouse form:

        * Give her/him a first name   
        * Give her/him a last name   
        * Enter a maiden name   
        * give her/him a DOB   
        * Select gender   

        #### CLICKABLE BUTTONS : 
        * Next - saves changes to DB and moves to Children page
        * Skip - Moves to Children page

        #### LOGIC WALKTHROUGH FOR SPOUSE:

            # SETUP A SEARCH
            
            GET JOHNS ID AND INSERT TO SPOUSE AS SPOUSE

            INSERT SPOUSE RECORD
            GET RETURNED SPOUSE ID
            
            INSERT SPOUSE ID INTO JOHN IN SPOUSE FIELD.

    ---
    ---

    * **PAGE 4: Edit Children**:  
    The user will be taken to **edit_children**, where their children will be displayed in an editable form if present. Otherwise, a search will be needed to find their parents within the DB.  
    If they are not in DB, they will need to fill out the enter children form:
    
        * Give her/him a first name   
        * Give her/him a last name   
        * give her/him a DOB   
        * Select gender   

        ( DYNAMICALLY ADD ANOTHER CHILD INPUT - CLICK +CHILD BUTTON? )

        #### CLICKABLE BUTTONS : 
        * Next - saves changes to DB and moves to JOHNS Circle page.
        * Skip - Moves to JOHNS Circle page.


        #### LOGIC WALKTHROUGH FOR CHILDREN:

            # SETUP A SEARCH FOR JOHNS CHILDREN - DISPLAY IF FOUND

            # I WILL NOT KNOW HOW MANY CHILDREN THERE ARE AS HOPING TO ADD INPUTS DYNAMICALLY FOR CHILDREN (USING JS) AS REQUIRED
            # SO DO A LOOP? 

            FOR I IN RANGE OF 0 TO 50
                IF INPUT FROM FORM CHILD[ i ] EXISTS
                    CREATE CHILDREN IN A DICTIONARY
                    ADD DICTIONARY TO A LIST_OF_CHILDREN - WHICH IS A LIST OF DICTIONARIES

            # END RESULT HERE SHOULD HAVE A LIST DICTIONARIES CONTAINING ALL CHILDREN
            
            INSERT THE LIST_OF_CHILDREN INTO MongoDB

            THIS RETURNS A LIST OF THE IDS

            # UPDATE JOHN AND JOHNS SPOUSE
                BUILD A LIST CALLED ALL_SIBLINGS_IDS
                    INSERT INTO THE LIST, THE ID OF EACH CHILD
                ADD THE ALL_CHILDREN_IDS TO EACH PARENT INTO THE FIELD CHILDREN:

            # GET THE ID OF BOTH PARENTS
                WE CAN GET THIS FROM JOHN,  AND HIS LINK TO HIS SPOUSE
            
            # UPDATE EACH CHILD AS SIBLINGS OF EACH OTHER:


            ALL_CHILDREN_ID = [30011, 30012, 30013, 30014 ]

            CREATE A LIST OF CHILD SIBLINGS FOR EACH CHILD SIBLING, BUT NOT INCLUDING THEMSELVES
                MEANING: CHILD 30011, SHOULD HAVE A LIST OF SIBLINGS, NOT INCLUDING 30011.
                ADD FATHER AND MOTHER ID TO EACH CHILD
                

            # THAT SHOULD GET US TO THE STAGE WHERE WE HAVE A LIST CHILDREN OF JOHN AND HIS SPOUSE, WHICH IS LINKED BACK TO THEM.
                ALSO, EACH CHILD HAS A LINK TO THEIR PARENTS ID
            # A LIST OF CHILDREN ID'S SHOULD ALSO BE IN EACH PARENT.
            # AND EACH CHILD IS A SPOUSE OF THE OTHER