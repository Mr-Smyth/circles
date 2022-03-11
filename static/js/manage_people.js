/*jshint esversion: 6 */ 
document.addEventListener('DOMContentLoaded', function () {

    /** FUNCTION TO HANDLE OPENING OF DELETE PERSON CONTAINER FORM 
     *  AND CLOSING OF ALL OTHERS */
    const searchForm = document.querySelector(".search-button");
    searchForm.onclick = function () {
        document.querySelector(".search-button").style.display = "none";
        document.querySelector(".search-container").style.display = "block";
        document.querySelector(".delete-button").style.display = "block";
        document.querySelector(".delete-container").style.display = "none";
        document.querySelector(".change-password-button").style.display = "block";
        document.querySelector(".password-container").style.display = "none";
    };
    
    
    /** FUNCTION TO HANDLE OPENING OF THE DELETE EVERYONE FORM
     *  AND CLOSING OF ALL OTHER FORMS*/
    const deleteForm = document.querySelector(".delete-button");
    deleteForm.onclick = function () {
        document.querySelector(".delete-button").style.display = "none";
        document.querySelector(".delete-container").style.display = "block";
        document.querySelector(".search-button").style.display = "block";
        document.querySelector(".search-container").style.display = "none";
        document.querySelector(".change-password-button").style.display = "block";
        document.querySelector(".password-container").style.display = "none";
    };
    
    
    /** FUNCTION TO HANDLE OPENING OF CHANGE DELETE PASSWORD CONTAINER FORM
     *  AND CLOSING OF ALL OTHERS */
    const passForm = document.querySelector(".change-password-button");
    passForm.onclick = function () {
        document.querySelector(".change-password-button").style.display = "none";
        document.querySelector(".password-container").style.display = "block";
        document.querySelector(".search-button").style.display = "block";
        document.querySelector(".search-container").style.display = "none";
        document.querySelector(".delete-button").style.display = "block";
        document.querySelector(".delete-container").style.display = "none";
    };
    
    
    /** FUNCTION TO HANDLE CHECKING OF NEW PASSWORDS TO SEE IF THEY MATCH
     * IF THEY DO SET FORM VALIDITY TO TRUE */
    const repeat_pass = document.getElementById("repeat_new_password");
    repeat_pass.onblur = function() {
        const new_pass = document.getElementById("new_password").value;
        const retype_pass = document.getElementById("repeat_new_password").value;
        if (new_pass === retype_pass){
            repeat_pass.setCustomValidity('');
        }
        else{
            repeat_pass.setCustomValidity("Passwords Don't Match");
        }
    };
}); 



