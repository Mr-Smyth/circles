document.addEventListener('DOMContentLoaded', function () {
    const searchBtn= document.querySelector(".search-button")
    searchBtn.onclick = function () {
        document.querySelector(".search-button").style.display = "none";
        document.querySelector(".search-container").style.display = "block";
    }
});