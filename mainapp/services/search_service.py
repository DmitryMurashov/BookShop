from mainapp.models import Author, Book, Category
from itertools import chain, groupby, _grouper


def search_for_all(query: str) -> (dict, int):
    data = {}
    quantity = 0

    for key, group in groupby(filter(lambda obj: query.lower() in obj.name.lower(), chain(Author.objects.all(), Book.objects.all(), Category.objects.all())), key=lambda x: type(x)):
        group_items = list(group)
        data[key] = group_items
        quantity += len(group_items)
    return data, quantity


def search_for_authors():
    pass


def search_for_books():
    pass
