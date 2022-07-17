from django.views.generic import DetailView, ListView, TemplateView
from mainapp.models import Book, Author, Category
from mainapp.services import search_service
from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


class IndexView(TemplateView):
    template_name = "mainapp/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        books = Book.objects.all()
        context['special_books'] = list(enumerate(books[:4]))
        context['books'] = books[:5]
        return context


class AboutView(TemplateView):
    template_name = 'mainapp/about.html'


class SearchView(TemplateView):
    template_name = "mainapp/search.html"

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        query = self.request.GET.get('query', "")
        context['query'] = query
        context['results_quantity'] = 0
        search_result, _ = search_service.search_for_all(query)
        search_for = self.request.GET.get("type")
        if search_for == "author":
            category = self.request.GET.get('category')
            context['authors'] = tuple(filter(
                lambda x: (not category or x.category.slug == category), search_result.get(Author)
            ))

        elif search_for == "book":
            author = self.request.GET.get("author")
            category = self.request.GET.get("category")
            context['books'] = tuple(filter(
                lambda x: (not author or x.author.slug == author) and (not category or x.category.slug == category),
                search_result.get(Book)))
        elif search_for == 'category':
            context['category'] = search_result.get(Category)
        else:
            context['authors'] = search_result.get(Author)
            context['books'] = search_result.get(Book)
            context['categories'] = search_result.get(Category)

        if authors := context.get("authors"):
            context['results_quantity'] += len(authors)
        if books := context.get("books"):
            context['results_quantity'] += len(books)
        if categories := context.get("categories"):
            context['results_quantity'] += len(categories)

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


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        if self.request.GET.get("action") == 'edit':
            return render(request, "mainapp/include/edit_profile_info.html", context={"profile": self.request.user.customer.profile})
        return render(request, "mainapp/profile.html", context={"profile": self.request.user.customer.profile})

    def post(self, request, *args, **kwargs):
        user = request.user
        profile = user.customer.profile

        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')

        profile.phone = request.POST.get('phone')
        profile.age = request.POST.get('age')

        user.save()
        profile.save()
        return HttpResponseRedirect(reverse('mainapp:profile'))
