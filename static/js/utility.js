/*jshint esversion: 6 */ 
document.addEventListener('DOMContentLoaded', function () {

    /* MATERIALIZE OPTIONS */
    let sidenavs = document.querySelectorAll(".sidenav");
    let sidenavsInstance = M.Sidenav.init(sidenavs, {edge: "right", draggable: "true"});
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);
    let datepickers = document.querySelectorAll(".datepicker");
    let datepickersInstance = M.Datepicker.init(datepickers, {
        format: "dd mmmm yyyy",
        yearRange: 150,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
    let collapsibles = document.querySelectorAll(".collapsible");
    let collapsiblesInstance = M.Collapsible.init(collapsibles);

    
     /** MAKE SELECT FEATURE HAVE VALIDATION 
      * CREDIT TIM IN CODE INSTITUTE FOR THIS CODE FROM THE COURSE
      * MINI PROJECT TO GET MATERIALIZE DROP DOWN OPTION LISTS TO HAVE
      * VALIDATION     */
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        /** Set up to new variables that will match the materialize validation */
        let classValid = "border-bottom: 1px solid #4caf50; box-shadow: 0 1px 0 0 #4caf50;";
        let classInvalid = "border-bottom: 1px solid #f44336; box-shadow: 0 1px 0 0 #f44336;";

        let selectValidate = document.querySelector("select.validate");
        let selectWrapperInput = document.querySelector(".select-wrapper input.select-dropdown");

        /** IF ANY SELECT ELEMENT HAS THE PROPERTY - REQUIRED - WE NEED TO UNHIDE IT
         * BUT MAKE IT INVISIBLE BY BASICALLY GIVING IT A WIDTH AND HEIGHT OF 0
         * MATERIALIZE HIDES SELECT ELEMENTS, BUT WE NEED THEM ON THE DOM.
         * AND BECAUSE IT IS ON THE DOM, IT WILL NOT ALLOW SUBMIT, AS IT IS REQUIRED
        */
        if (selectValidate != null && selectValidate.hasAttribute("required")) {
            selectValidate.style.cssText = "display: block; height: 0; padding: 0; width: 0; position: absolute;";
        }

        
        /** ONCE THE USER IS FOCUSED ON THE INPUT SECTION OF THE SCREEN 
         * WE TRAVERSE THE DOM UP AND DOWN USING PARENT AND CHILD EVENT LISTENERS
         * IF ONE OF THE LIST ITEMS IS SELECTED, BUT DOESNT HAVE THE DISABLED 
         * ATTRIBUTE, THEN APPLY THE CLASS classValid TO MAKE IT GREEN
        */
        if (selectWrapperInput != null) {
            selectWrapperInput.addEventListener("focusin", (e) => {
                e.target.parentNode.addEventListener("change", () => {
                    let ulSelectOptions = e.target.parentNode.childNodes[1].childNodes;
                    for (let i = 0; i < ulSelectOptions.length; i++) {
                        if (ulSelectOptions[i].className == "selected" && ulSelectOptions[i].hasAttribute != "disabled") {
                            e.target.style.cssText = classValid;
                        }
                    }
                });
            });

            /** ADD EVENT LISTENER TO WRAPPER INPUT ELEMENTS - FOR A CLICK
             * WE TRAVERSE THE DOM UP AND DOWN USING PARENT AND CHILD EVENT LISTENERS
             * IF sELECTED ITEM HAS CLASS OF SELECTED AND IS NOT DISABLED then 
             * CLASS IS VALID AND SO THE LINE REMAINS GREEN
             * ELSE IF THE FOCUS LEAVES THE LIST, THE CLASS BECOMES INVALID, AND
             * SO THE LINE IS RED.
             * I THINK THIS IS FOR CASES WHEN REENTERING THE LIST?
             */
            selectWrapperInput.addEventListener("click", (e) => {
                let ulSelectOptions = e.target.parentNode.childNodes[1].childNodes;
                for (let i = 0; i < ulSelectOptions.length; i++) {
                    if (ulSelectOptions[i].className == "selected" && ulSelectOptions[i].hasAttribute != "disabled" && ulSelectOptions[i].style.backgroundColor == "rgba(0, 0, 0, 0.03)") {
                        e.target.style.cssText = classValid;
                    } else {
                        e.target.addEventListener("focusout", () => {
                            if (e.target.parentNode.childNodes[3].hasAttribute("required")) {
                                if (e.target.style.borderBottom != "1px solid rgb(76, 175, 80)") {
                                    e.target.style.cssText = classInvalid;
                                }
                            }
                        });
                    }
                }
            });
        }
    }
});

/** SWITCH OFF THE LOADER WHEN PAGE LOADS */
window.addEventListener('load',function(){
    overlay.style.display = 'none';
});


