import random
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from .models import CustomUser
from django.views.generic import TemplateView

class UserPageView(TemplateView):
    template_name = 'users/user_page.html'

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        # Отправка письма для верификации почты
        send_mail(
            'Welcome!',
            'Thank you for registering.',
            'from@example.com',
            [user.email],
            fail_silently=False,
        )
        return super().form_valid(form)

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

class PasswordResetView(CreateView):
    template_name = 'users/password_reset.html'

    def post(self, request, **kwargs):
        email = request.POST.get('email')
        try:
            user = CustomUser.objects.get(email=email)
            new_password = str(random.randint(100000, 999999))
            user.password = make_password(new_password)
            user.save()

            send_mail(
                'Сброс пароля',
                f'Ваш новый пароль: {new_password}',
                'from@example.com',
                [email],
                fail_silently=False,
            )
            return HttpResponse('Пароль сброшен! Проверьте почту.')
        except CustomUser.DoesNotExist:
            return HttpResponse('Пользователь с такой почтой не найден.')

