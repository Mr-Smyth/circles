document.addEventListener('DOMContentLoaded', function () {
    const searchForm = document.querySelector(".search-button")
    searchForm.onclick = function () {
        document.querySelector(".search-button").style.display = "none";
        document.querySelector(".search-container").style.display = "block";
    }
});


