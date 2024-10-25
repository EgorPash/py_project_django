from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.translation.trans_real import catalog

from users.apps import UsersConfig
from users.views import RegisterView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy("users:login")), name='logout'),
    path('register/', RegisterView.as_view(), name='register')
]