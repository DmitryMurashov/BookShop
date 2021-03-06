from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from authapp.models import Customer
from django.core.validators import MaxValueValidator, MinValueValidator
from itertools import chain
User = get_user_model()


class Book(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name="books")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="books")
    price = models.DecimalField(max_digits=9, decimal_places=2)
    name = models.CharField(max_length=50)
    demo = models.TextField(max_length=1000, null=True)
    description = models.TextField(null=True)
    short_description = models.TextField(max_length=200)
    image = models.ImageField()
    slug = models.SlugField(max_length=60)

    def get_absolute_url(self):
        return reverse("mainapp:book_detail", kwargs={"slug": self.slug})

    def get_reviews_page(self):
        return reverse("mainapp:book_reviews", kwargs={"slug": self.slug})

    def set_slug(self):
        self.slug = f"Book{self.id}"

    @property
    def rating(self) -> int:
        reviews = self.book_reviews.all()
        try:
            rating = round(sum(review.stars for review in reviews) / len(reviews))
        except ZeroDivisionError:
            return 0
        return rating

    @property
    def rating_as_stars(self):
        return chain(["bi bi-star-fill" for _ in range(self.rating)], ["bi bi-star" for _ in range(5 - self.rating)])

    def get_reviews(self, positive_filter: bool = False, negative_filter: bool = False) -> list:
        reviews = self.book_reviews.all()
        if positive_filter:
            reviews = sorted(reviews, key=lambda x: x.stars, reverse=True)
        elif negative_filter:
            reviews = sorted(reviews, key=lambda x: x.stars)
        return list(reviews)

    def __str__(self):
        return f"Book[{self.name}]"


class Author(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    biography = models.TextField()
    image = models.ImageField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="authors")
    slug = models.SlugField(max_length=110)

    def __str__(self):
        return f"Author[{self.full_name}]"

    def get_absolute_url(self):
        return reverse('mainapp:author_detail', kwargs={'slug': self.slug})

    def get_reviews_page(self):
        return reverse("mainapp:author_reviews", kwargs={"slug": self.slug})

    def set_slug(self) -> None:
        self.slug = f"Author{self.id}"

    @property
    def full_name(self) -> str:
        return f"{self.name} {self.last_name}"

    @property
    def books_page_url(self) -> str:
        return reverse('mainapp:search') + f"?type=book&author={self.slug}"


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    description = models.TextField(null=True)
    slug = models.SlugField(max_length=50)

    def set_slug(self) -> None:
        self.slug = f"Category{self.id}"

    @property
    def books_page_url(self) -> str:
        return reverse('mainapp:search') + f"?type=book&category={self.slug}"

    @property
    def authors_page_url(self) -> str:
        return reverse('mainapp:search') + f"?type=author&category={self.slug}"


class BookReview(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name="customer_book_reviews")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_reviews")
    content = models.TextField(max_length=1000)
    stars = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
