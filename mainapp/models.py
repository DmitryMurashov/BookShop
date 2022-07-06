from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()


class Book(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name="books")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="books")
    price = models.DecimalField(max_digits=9, decimal_places=2)
    name = models.CharField(max_length=50)
    demo = models.TextField(max_length=1000, null=True)
    description = models.TextField(null=True)
    image = models.ImageField()
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})


class Author(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    biography = models.TextField()
    image = models.ImageField()
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'slug': self.slug})

    @property
    def full_name(self):
        return f"{self.name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
