from mainapp.models import Book


def get_book(slug):
    return Book.objects.get(slug=slug)


def get_most_popular_books():
    return list(sorted(Book.objects.all(), key=lambda x: len(x.get_reviews())))[:10]
