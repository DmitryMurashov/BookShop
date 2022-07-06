const show_demo = document.getElementById('show_demo')
const demo_text_div = document.getElementById('demo_text')
demo_text_div.style.visibility = "hidden"

show_demo.addEventListener("click", function (event) {
    if (demo_text_div.style.visibility === "hidden") {
        demo_text_div.style.visibility = "visible"
        show_demo.innerText = "Скрыть отрывок"
    } else {
        demo_text_div.style.visibility = "hidden"
        show_demo.innerText = "Показать отрывок"
    }
})