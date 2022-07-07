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
    slug = models.SlugField(max_length=60)

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})

    def set_slug(self):
        self.slug = f"Book{self.id}"

    def __str__(self):
        return f"Book[{self.name}]"


class Author(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    biography = models.TextField()
    image = models.ImageField()
    slug = models.SlugField(max_length=110)

    def __str__(self):
        return f"Author[{self.full_name}]"

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'slug': self.slug})

    def set_slug(self) -> None:
        self.slug = f"Author{self.id}"

    @property
    def full_name(self) -> str:
        return f"{self.name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def set_slug(self) -> None:
        self.slug = f"Category{self.id}"



