from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView, PasswordResetForm

app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='users:login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('password_reset/', PasswordResetForm.as_view(template_name='users/password_reset.html'), name='password_reset'),
]