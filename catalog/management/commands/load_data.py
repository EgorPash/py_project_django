from django.core.management.base import BaseCommand
from catalog.models import Category, Product
import json

class Command(BaseCommand):
    help = 'Load data from json files'

    def handle(self, *args, **options):
        # Очистка таблиц перед загрузкой данных
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Загрузка категорий
        with open('catalog/fixtures/categories.json') as f:
            data = json.load(f)
            for item in data:
                Category.objects.create(id=item['pk'], name=item['fields']['name'], description=item['fields']['description'])

        # Загрузка продуктов (попробуйте здесь обращаться к категориям)
        # Например:
        category_id = 1  # Убедитесь, что категория с этим ID существует
        try:
            category = Category.objects.get(pk=category_id)
            Product.objects.create(name='Smartphone', description='Latest model', category=category, price=699.99)
        except Category.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Category with ID {category_id} does not exist!'))