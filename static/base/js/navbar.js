const searchInput = document.getElementById('searchbar')
const searchButton = document.getElementById('search-btn-submit')

searchButton.addEventListener('click', function (_) {
    let query = searchInput.value
    if (query) {
        location.href = `/search/?query=${query}`
    }
})