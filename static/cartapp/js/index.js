function update_events() {
    let cart_products_div = document.getElementById('cart_products')
    let cartDiv = document.getElementById('CartWrapper')
    let csrfToken = document.cookie.substring(document.cookie.indexOf('=') + 1)
    cart_products_div.addEventListener('input', function (target) {
        if (target.target.nodeName === 'INPUT' && target.target.type === 'number') {
            $.ajax({
                type: "POST",
                url: 'http://127.0.0.1:8000/cart/set/',
                data: {
                    'slug': target.target.name,
                    'quantity': target.target.value
                },
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrfToken
                },
                success: function (data, _) {
                    cartDiv.innerHTML = data
                    update_events()  // TODO
                }
            })
        }
    })
    cart_products_div.addEventListener("click", function (target) {
        if (target.target.nodeName === 'BUTTON' && target.target.name === 'delete_product') {
            $.ajax({
                type: "POST",
                url: 'http://127.0.0.1:8000/cart/delete/',
                data: {
                    'slug': target.target.value
                },
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrfToken
                },
                success: function (data, _) {
                    cartDiv.innerHTML = data
                    update_events()
                }
            })
        }
    })
}

update_events()
