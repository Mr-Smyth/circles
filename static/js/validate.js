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
    /** LISTEN FOR FORM SUBMIT*/
    const form = document.getElementsByName("form")[0];
    form.addEventListener('submit', validateform);   
});

/** SWITCH OFF THE LOADER WHEN PAGE LOADS */
let overlay = document.getElementById("overlay");
window.addEventListener('load',function(){
    overlay.style.display = 'none';
});

