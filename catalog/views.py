from django.shortcuts import render
from django.shortcuts import get_object_or_404
from catalog.models import Product


def home_view(request):
    products = Product.objects.all()  # Получаем все продукты
    context = {'products': products}  # Формируем контекст
    return render(request, 'catalog/home.html', context)

def contact_view(request):
    return render(request, 'catalog/contact.html')

def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)  # Получаем продукт по pk или 404
    context = {'object': product}  # Формируем контекст
    return render(request, 'catalog/product_detail.html', context)