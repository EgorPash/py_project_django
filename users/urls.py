from django.urls import path
from .views import RegisterView, CustomLoginView, HomePageView, PasswordResetView

app_name = 'users'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('password_reset', PasswordResetView.as_view(), name='password_reset'),
]