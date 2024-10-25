from django.contrib.auth import login
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings

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

