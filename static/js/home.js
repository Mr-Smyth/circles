document.addEventListener('DOMContentLoaded', function () {
    const searchForm = document.querySelector(".search-button")
    searchForm.onclick = function () {
        document.querySelector(".search-button").style.display = "none";
        document.querySelector(".search-container").style.display = "block";
    }
    const deleteForm = document.querySelector(".delete-button")
    deleteForm.onclick = function () {
        document.querySelector(".delete-button").style.display = "none";
        document.querySelector(".delete-container").style.display = "block";
    }

});


