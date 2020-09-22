document.addEventListener('DOMContentLoaded', function () {
    let sidenavs = document.querySelectorAll(".sidenav");
    let sidenavsInstance = M.Sidenav.init(sidenavs, {edge: "right", draggable: "true"});
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);
    let datepickers = document.querySelectorAll(".datepicker");
    let datepickersInstance = M.Datepicker.init(datepickers, {
        format: "dd mmmm, yyyy",
        yearRange: 150,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
});