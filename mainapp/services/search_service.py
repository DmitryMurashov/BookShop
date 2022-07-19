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


def filter_authors(search_result: dict, category: str = None):
    return tuple(filter(lambda x: (not category or x.category.slug == category), search_result.get(Author)))


def filter_books(search_result: dict, author: str = None, category: str = None) -> tuple:
    return tuple(filter(lambda x: (not author or x.author.slug == author) and (not category or x.category.slug == category), search_result.get(Book)))
