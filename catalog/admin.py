from django.contrib import admin
from django.contrib.auth.models import Group
from catalog.models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'user')
    search_fields = ('name', 'description')
    list_filter = ('is_published',)

admin.site.register(Product, ProductAdmin)
