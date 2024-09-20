/* -------------------------------------------------------------------
 * Template         : Rundal - Modern Multi-Purpose HTML5 Template
 * Author           : SeparateWeb
------------------------------------------------------------------- */
const text = document.querySelector(".round-text .texts")
window.addEventListener("scroll", function () {
    text.style.transform = `rotate(${window.scrollY * 0.20}deg)`
})