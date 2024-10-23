from django.db import models
from users.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manufactured_at = models.DateTimeField(null=True, blank=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
            ("can_change_description", "Can change product description"),
            ("can_change_category", "Can change product category"),
        ]

class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions')
    version_number = models.CharField(max_length=255)
    version_name = models.CharField(max_length=255)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.version_number} - {self.product.name}"
