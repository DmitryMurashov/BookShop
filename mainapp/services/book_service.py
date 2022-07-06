from mainapp.models import Book


def get_book(slug):
    return Book.objects.get(slug=slug)
