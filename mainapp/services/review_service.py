from mainapp.models import BookReview
from mainapp.services.book_service import get_book


def get_user_review(customer, book):
    try:
        return BookReview.objects.get(customer=customer, book=book)
    except BookReview.DoesNotExist:
        return


def create_review(request):
    book = get_book(request.POST.get('book_slug'))
    rating = request.POST.get("selected_rating")
    content = request.POST.get("review_content")
    customer = request.user.get_customer()
    try:
        BookReview.objects.get(customer=customer, book=book)
    except BookReview.DoesNotExist:
        review = BookReview(customer=customer, book=book, content=content, stars=rating)
        review.save()
        return review


def edit_review(request):
    rating = int(request.POST.get("selected_rating"))
    content = request.POST.get("review_content")
    if review_id := request.POST.get("review_id"):
        review_id = int(review_id)
        try:
            review = BookReview.objects.get(id=review_id)
        except BookReview.DoesNotExist:
            return
    else:
        book = get_book(request.POST.get("book_slug"))
        customer = request.user.get_customer()
        review = BookReview.objects.get(book=book, customer=customer)
    review.content = content
    review.stars = rating
    review.save()
    return review
