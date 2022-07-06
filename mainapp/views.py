from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views import View
from mainapp.models import Book, Author
from mainapp.services import book_service


class IndexPage(View):
    def get(self, request, **kwargs):
        books = Book.objects.all()
        authors = Author.objects.all()
        return render(request, "mainapp/index.html", context={"books": books, "authors": authors})


class BooksView(ListView):
    model = Book
    context_object_name = "books"


class BookDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        book = book_service.get_book(kwargs.get("slug"))
        return render(request, "mainapp/book_detail.html", context={"book": book})


class AuthorsView(ListView):
    model = Author
    context_object_name = "Authors"


class AuthorDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        author = book_service.get_book(kwargs.get("slug"))
        return render(request, "mainapp/book_detail.html", context={"author": author})
