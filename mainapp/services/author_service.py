from mainapp.models import Author


def get_author(slug):
    return Author.objects.get(slug=slug)


def get_most_popular_authors():
    return Author.objects.all()[:10]
