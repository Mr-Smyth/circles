/*jshint esversion: 6 */ 
document.addEventListener('DOMContentLoaded', function () {
    
    /** THIS FUNCTION STOPS FORM SUBMISSION UNLESS FORM IS VALIDATED
    SPECIFICALLY CHECKING DATE OF BIRTH, AS IT IS SET TO READONLY IN HTML
    AND SO REQUIRED SOME MANUAL VALIDATION */
    function validateform(e) { 
        e.preventDefault();
        const formStatus = document.querySelector("form").checkValidity();
        let dobStatus = document.getElementById("dob");
        
        if (dobStatus === null){
            /** THEN WE ARE ON THE PARENTS PAGE  */
            let motherdob = document.getElementById("mothers_dob");  
            let fatherdob = document.getElementById("fathers_dob"); 
        
            /**IF MOTHER HAS NO DOB */
            if (motherdob.value === "") {
                motherdob.focus();
                motherdob.placeholder = "Please Enter Date of Birth";
                motherdob.classList.add("warning-text");
            }
            /**IF FATHER HAS NO DOB */
            else if(fatherdob.value === ""){
                fatherdob.focus();
                fatherdob.placeholder = "Please Enter Date of Birth";
                fatherdob.classList.add("warning-text");
            }
            /** THEY BOTH HAVE A DOB AND FORM STATUS IS TRUE - CARRY ON */
            else {
                if (formStatus == true){
                    form.submit();
                    /** Switch on loader */
                    let overlay = document.getElementById("overlay");
                    overlay.style.display = "flex";
                }
            }
            return;
        }
        /** HANDLES ALL OTHER FORM PAGES */
        if (dobStatus.value === "") {
            dobStatus.focus();
            dobStatus.placeholder = "Please Enter the Date of Birth";
            dobStatus.classList.add("warning-text");
            
        } 
        /** FORM STATUS IS TRUE - CARRY ON */
        else {
            if (formStatus == true){
                form.submit();
                /** Switch on loader */
                let overlay = document.getElementById("overlay");
                overlay.style.display = "flex";
            }
        }
    }
    /** LISTEN FOR FORM SUBMIT - ACTIVATES ABOVE CODE*/
    const form = document.getElementsByName("form")[0];
    form.addEventListener('submit', validateform);

    /** VALIDATE THE READONLY DATE PICKERS WITH THE 
     * GREEN OR RED LINES GET DOB INPUT - AS THE PARENTS PAGE
     * HAS 2 DOB DATEPICKERS IN ONE FORM, I NEED TO CHECK FOR THIS */
    if (document.getElementById("fathers_dob")){
        const dob = document.getElementById("fathers_dob");
        dob.addEventListener("click", function(){
            checkColour(dob);
        });
    }
    if (document.getElementById("mothers_dob")){
        const dob = document.getElementById("mothers_dob");
        dob.addEventListener("click", function(){
            checkColour(dob);
        });
    }
    if (document.getElementById("dob")){
        const dob = document.getElementById("dob");
        dob.addEventListener("click", function(){
           checkColour(dob);
        });
    }

    /* CHECKS WHAT COLOR TO APPLY TO THE DOB INPUT ELEMENT */
    function checkColour(dob, repeat = true){
        /* SET A DEFAULT COLOR BEFORE CHANGES */
        if (dob.value == ""){
            dob.style.borderBottom = "1px solid red";
            dob.style.boxShadow = "0px 1px 0px 0px red";
        }
        else {
            dob.style.borderBottom = "1px solid #4CAF50";
            dob.style.boxShadow = "0px 1px 0px 0px #4CAF50";
        }
        /** CHECK IF WE CAN REPEAT CALL TO HANDLEMODAL() */
        if (repeat){
            handleModal(dob);
        }
        else{
            return;
        }
    }
    /** ACT UPON WHAT USER DOES IN THE DATEPICKER MODAL */
    function handleModal(dob){
        /** GET THE DOB PARENT NODE - 
         * BECAUSE THE MODEL I WANT IS CONTAINED IN THE PARENT NODE OF THE DOB I CLICKED ON.
         * NOT IN THE DOB ELEMENT. i NEED TO MAKE SURE JS ISNT LOOKING AT THE WRONG MODAL 
         * WHEN THE USER CLICKS SUBMIT OR CLEAR. - REQUIRED FOR PARENT PAGE WHERE THERE ARE 2 
         * DOB 'S - I NEED TO KNOW WHICH MODAL IM CLICKING BUTTONS ON.*/
        let parent = dob.parentNode;
        /** SETTING REPEAT TO FALSE WILL STOP chechColour CALLING THIS FUNCTION AGAIN. */
        let repeat = false;
        /* LISTEN FOR THE MODAL TO BE CLOSED PROPERLY WITH A SELECTION -
        THEN CALL checkColour AGAIN TO SET CORRECT COLOUR*/
        parent.querySelector(".datepicker-cancel").addEventListener("click", function(){
            checkColour(dob, repeat);
        });
        parent.querySelector(".datepicker-done").addEventListener("click", function(){
            checkColour(dob, repeat);
        });
        parent.querySelector(".datepicker-clear").addEventListener("click", function(){
            checkColour(dob, repeat);
        });
    }
});

/** SWITCH OFF THE LOADER WHEN PAGE LOADS */
let overlay = document.getElementById("overlay");
window.addEventListener('load',function(){
    overlay.style.display = 'none';
});
