from django.views.generic import DetailView, ListView, TemplateView
from mainapp.models import Book, Author


class IndexView(TemplateView):
    template_name = "mainapp/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context["page_title"] = "Главная"
        return context


class SearchView(TemplateView):
    template_name = "mainapp/search.html"

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data()
        context["books"] = Book.objects.all()
        context["authors"] = Author.objects.all()
        context["page_title"] = "Поиск"
        return context


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
