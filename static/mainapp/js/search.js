const inputSearch = document.getElementById("inputSearch")
const elements_list = document.getElementById("elements")

let elements = elements_list.getElementsByTagName('li')
for (let index = 0; index < elements.length; index++) {
    elements[index].style.display = "none"
}

inputSearch.addEventListener('input', function (event) {
    let query = event.target.value.toLowerCase()
    let elements = elements_list.getElementsByTagName('li')
    for (let index = 0; index < elements.length; index++) {
        let element = elements[index]
        let link = element.getElementsByTagName('a')[0]
        if (query !== "" && link.text.toLowerCase().indexOf(query) > -1) {
            element.style.display = ""
        } else {
            element.style.display = "none"
        }
    }
})
