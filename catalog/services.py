from django.core.cache import cache
from catalog.models import Category

def get_categories():
    categories = cache.get('categories')
    if not categories:
        categories = list(Category.objects.all())
        cache.set('categories', categories, timeout=60 * 15)  # кеш на 15 минут
    return categories