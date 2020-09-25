document.addEventListener('DOMContentLoaded', function () {
    myForm = document.querySelector(".search-button")
    myForm.onclick = function () {
        document.querySelector(".search-button").style.display = "none";
        document.querySelector(".container").style.display = "block";
    }

});


