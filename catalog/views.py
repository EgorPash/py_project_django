from django.shortcuts import render

def home_view(request):
    return render(request, 'catalog/templates/home.html')

def contact_view(request):
    return render(request, 'catalog/templates/contact.html')
