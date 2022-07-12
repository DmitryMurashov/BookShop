const buy_buttons = document.querySelectorAll('button[name=buyButton]')
const csrfToken = document.cookie.substring(document.cookie.indexOf('=') + 1);


buy_buttons.forEach(function (button) {
    button.addEventListener('click', function (_) {
        $.ajax({
            type: "POST",
            url: 'http://127.0.0.1:8000/cart/add/',
            data: {
                'slug': button.value
            },
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': csrfToken
            },
            success: function () {
                showToast('Добавлено в <a href="http://127.0.0.1:8000/cart/">карзину</a>', {  // Написать свою библеотеку
                    duration: 5000,
                    borderRadius: '25px',
                    background: '#61bb03',
                    close: true
                });
            }
        });

    })
})
