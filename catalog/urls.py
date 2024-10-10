from django.urls import path, include
from catalog import views

app_name = 'catalog'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('blog/', include('blog.urls', namespace='blog')),  # Подключаем блог
]
