from django.urls import path
from mainapp import views as mainapp

urlpatterns = [
    path('', mainapp.IndexPage.as_view(), name="index"),
    path('books/', mainapp.BooksView.as_view(), name="books"),
    path('books/book/', mainapp.BookDetailView.as_view(), name="book_detail"),
    path('authors/', mainapp.AuthorsView.as_view(), name="authors"),
    path('authors/author/', mainapp.AuthorsView.as_view(), name="author_detail")
]
