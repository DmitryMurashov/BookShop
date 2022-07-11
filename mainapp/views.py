from django.views.generic import DetailView, ListView, TemplateView
from mainapp.models import Book, Author, Category
from mainapp.services import search_service


class IndexView(TemplateView):
    template_name = "mainapp/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        books = Book.objects.all()
        context['special_books'] = list(enumerate(books))
        context['books'] = books
        return context


class AboutView(TemplateView):
    template_name = 'mainapp/about.html'


class SearchView(TemplateView):
    template_name = "mainapp/search.html"

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        query = self.request.GET.get('query')
        context['query'] = query
        search_result, quantity = search_service.search_for_all(query)
        context['results_quantity'] = quantity
        context["books"] = search_result.get(Book)
        context["authors"] = search_result.get(Author)
        context["categories"] = search_result.get(Category)
        return context


class BooksView(ListView):
    model = Book
    template_name = "mainapp/books.html"
    context_object_name = "books"


class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"
    template_name = "mainapp/book_detail.html"
    slug_url_kwarg = "slug"


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
