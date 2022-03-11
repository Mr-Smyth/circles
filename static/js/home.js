/*jshint esversion: 6 */ 
document.addEventListener('DOMContentLoaded', function () {

    /* HERE WE DISPLAY THE HOME PAGE SEARCH FORM AND ALSO HIDE SEARCH BUTTON */
    const searchBtn= document.querySelector(".search-button");
    searchBtn.onclick = function () {
        document.querySelector(".search-button").style.display = "none";
        document.querySelector(".search-container").style.display = "block";
    };
});
