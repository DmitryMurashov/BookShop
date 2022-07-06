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
    template_name = "mainapp/books.html"
    context_object_name = "books"

    def get_context_data(self, **kwargs):
        context = super(BooksView, self).get_context_data(**kwargs)
        context["page_title"] = "Книги"
        return context


class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"
    template_name = "mainapp/book_detail.html"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        context["page_title"] = self.get_object().name
        return context


class AuthorsView(ListView):
    model = Author
    context_object_name = "authors"
    template_name = "mainapp/authors.html"

    def get_context_data(self, **kwargs):
        context = super(AuthorsView, self).get_context_data(**kwargs)
        context["page_title"] = "Авторы"
        return context


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = "author"
    template_name = "mainapp/author_detail.html"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        author = self.get_object()
        context["books"] = author.books
        context["page_title"] = author.full_name
        return context
