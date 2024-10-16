from django.urls import path, include
from catalog import views

app_name = 'catalog'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('create/', views.ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('version/create/', views.VersionCreateView.as_view(), name='version_create'),
    path('version/update/<int:pk>/', views.VersionUpdateView.as_view(), name='version_update'),
]
