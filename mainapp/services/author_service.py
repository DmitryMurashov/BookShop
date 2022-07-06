from mainapp.models import Author


def get_author(slug):
    return Author.objects.get(slug=slug)
