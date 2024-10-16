from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.core.mail import send_mail
from .forms import RegistrationForm
from django.conf import settings
from django.utils.crypto import get_random_string

class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            send_mail(
                'Welcome to Our Site',
                'Thank you for registering!',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
            )
            login(request, user)
            return redirect('catalog:home')
        return render(request, 'users/register.html', {'form': form})
