from django.urls import path
from catalog import views

app_name = 'catalog'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('product/<int:pk>/', views.product_detail_view, name='product_detail'),
]
