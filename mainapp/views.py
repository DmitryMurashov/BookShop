from django.views.generic import DetailView, TemplateView
from mainapp.models import Book, Author, Category
from mainapp.services import search_service, book_service, author_service, review_service
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
        search_for = self.request.GET.get("type")
        context['query'] = query
        context['results_quantity'] = 0
        if query == "" and not search_for:
            return context
        search_result, quantity = search_service.search_for_all(query)
        if search_for == "author":
            category = self.request.GET.get('category')
            authors = search_service.filter_authors(search_result, category=category)
            context['authors'] = authors
            context['results_quantity'] += len(authors)
        elif search_for == "book":
            author, category = self.request.GET.get("author"), self.request.GET.get("category")
            books = search_service.filter_books(search_result, author=author, category=category)
            context['books'] = books
            context['results_quantity'] += len(books)
        elif search_for == 'category':
            categories = search_result.get(Category)
            context['category'] = categories
            context['results_quantity'] += len(categories)
        else:
            authors = search_result.get(Author)
            books = search_result.get(Book)
            categories = search_result.get(Category)
            context['authors'] = authors
            context['books'] = books
            context['categories'] = categories
            context['results_quantity'] = quantity
        return context


class BooksView(TemplateView):
    template_name = "mainapp/books.html"

    def get_context_data(self, **kwargs):
        context = super(BooksView, self).get_context_data(**kwargs)
        context['books'] = book_service.get_most_popular_books()
        return context


class BookDetailView(View):
    def get(self, request, *args, **kwargs):
        book = book_service.get_book(kwargs.get("slug"))
        context = {
            "book": book,
            "reviews": book.get_reviews(positive_filter=True)[:10],
            "user_review": review_service.get_user_review(request.user.get_customer(), book),
        }
        return render(request, "mainapp/book_detail.html", context=context)


class CreateReviewView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('mainapp:main')))

    def post(self, request, *args, **kwargs):
        review_service.create_review(request)
        return HttpResponseRedirect(request.META.get("PATH_INFO"))


class EditReviewView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('mainapp:main')))

    def post(self, request, *args, **kwargs):
        review_service.edit_review(request)
        return HttpResponseRedirect(request.META.get("PATH_INFO"))


class DeleteReviewView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('mainapp:main')))

    def post(self, request, *args, **kwargs):
        pass


class RateViewView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('mainapp:main')))

    def post(self, request, *args, **kwargs):
        pass


class AuthorsView(TemplateView):
    template_name = "mainapp/authors.html"

    def get_context_data(self, **kwargs):
        context = super(AuthorsView, self).get_context_data(**kwargs)
        context['authors'] = author_service.get_most_popular_authors()
        return context


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = "author"
    template_name = "mainapp/author_detail.html"
    slug_url_kwarg = "slug"


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        if self.request.GET.get("action") == 'edit':
            return render(request, "mainapp/include/profile/edit_profile_info.html", context={"customer": request.user.get_customer(request.user)})
        return render(request, "mainapp/profile.html", context={"customer": request.user.get_customer()})

    def post(self, request, *args, **kwargs):
        user = request.user
        customer = user.customer

        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')

        customer.phone = request.POST.get('phone')
        customer.age = request.POST.get('age')

        user.save()
        customer.save()
        return HttpResponseRedirect(reverse('mainapp:profile'))
