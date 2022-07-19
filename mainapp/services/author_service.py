from mainapp.models import Author


def get_author(slug):
    return Author.objects.get(slug=slug)


def get_most_popular_authors():
    return list(sorted(Author.objects.all(), key=lambda x: len(x.get_reviews())))[:10]
