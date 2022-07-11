from django.urls import path
from mainapp import views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.IndexView.as_view(), name="main"),
    path('search/', mainapp.SearchView.as_view(), name="search"),
    path('books/', mainapp.BooksView.as_view(), name="books"),
    path('books/book/<slug:slug>/', mainapp.BookDetailView.as_view(), name="book_detail"),
    path('authors/', mainapp.AuthorsView.as_view(), name="authors"),
    path('authors/author/<slug:slug>/', mainapp.AuthorDetailView.as_view(), name="author_detail"),
    path('about/', mainapp.AboutView.as_view(), name='about'),
]
