// function boxClicked(event) {
//     let box = document.getElementsByClassName(‘box’);
//        // for (let i = 0; i < box.length; i++) {
//         for (let i in box) {
//             this[i].addEventListener(“click”, boxClicked);
//             if ( this[i].style.backgroundColor == ‘orange’) {
//                 this[i].style.backgroundColor = ‘green’;
//             } else  {
//                 this[i].style.backgroundColor = ‘orange’;
//                 }
//         }
//     }


let box = document.querySelectorAll('.row')
box.forEach((btn) => {
  btn.addEventListener("click", (event) => {
    alert(event.target);
  });
});