const csrfToken = document.cookie.substring(document.cookie.indexOf('=') + 1);

$(".btn-rating").on('click', (function (_) {
    let rating_element = $("#selected_rating")
    let previous_value = rating_element.val();
    let selected_value = $(this).attr("data-attr");

    rating_element.val(selected_value);
    for (let i = 1; i <= selected_value; ++i) {
        let element = $("#rating-star-" + i)
        element.toggleClass('btn-warning text-dark');
        element.toggleClass('btn-default text-gray');
    }

    for (let i = 1; i <= previous_value; ++i) {
        let element = $("#rating-star-" + i)
        element.toggleClass('btn-warning text-dark');
        element.toggleClass('btn-default text-gray');
    }
}))

$("#ReviewButton").on('click', function () {
    $('#ReviewModel').modal('show');
})

$("#EditReviewContentButton").on('click', (function (event) {
    $('#ReviewForm').attr('action', location.href + 'reviews/edit/')
    $('#ReviewModel').modal('show');
}))