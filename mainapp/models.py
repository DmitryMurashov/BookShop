from django.db import models
from django.contrib.auth import get_user_model
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


class Author(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    biography = models.TextField()
    image = models.ImageField()
    slug = models.SlugField()


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
