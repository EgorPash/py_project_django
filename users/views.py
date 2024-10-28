from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.views import PasswordResetView
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password

from users.forms import UserRegisterForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        # Сохраняем пользователя
        user = form.save()
        login(self.request, user)

        # Отправка email-уведомления
        self.send_confirmation_email(user.email)

        return super().form_valid(form)


    def send_confirmation_email(self, email):
        subject = 'Регистрация успешно завершена'
        message = 'Спасибо за регистрацию на нашем сайте. Мы рады видеть вас!'
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

class PasswordResetForm(TemplateView):
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            new_password = get_random_string(length=8)  # Генерация нового пароля
            user.password = make_password(new_password)  # Хеширование пароля
            user.save()
            self.send_confirmation_email(email, new_password)  # Отправка email с новым паролем
        except User.DoesNotExist:
            # Обработка случая, когда пользователь не найден
            pass
        return redirect("/")

    def send_confirmation_email(self, email, new_password):
        subject = 'Ваш новый пароль'
        message = f'Ваш новый пароль: {new_password}'
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )