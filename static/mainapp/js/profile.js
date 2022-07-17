const userInfoDiv = document.getElementById('userInfo')
const changeButton = document.getElementById("changeButton")
const csrfToken = document.cookie.substring(document.cookie.indexOf('=') + 1)


changeButton.addEventListener("click", function (_) {
    $.ajax({
        type: "GET",
        url: 'http://127.0.0.1:8000/profile/?action=edit',
        data: {},
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfToken
        },
        success: function (data, _) {
            userInfoDiv.innerHTML = data
        }
    })
    changeButton.remove()
})