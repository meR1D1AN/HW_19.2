import secrets
import random

from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout, login
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email_verification/{token}/'
        send_mail(
            subject='Активация аккаунта',
            message=f'Для активации аккаунта, перейдите по ссылке: {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')  # Перенаправляет на главную страницу


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class VerifyEmailView(View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.is_active = True
        user.save()
        login(request, user)
        return redirect(reverse('users:login'))


class PasswordResetView(View):
    def post(self, request):
        email = request.POST.get('email')
        user = get_object_or_404(User, email=email)
        new_password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=8))
        user.password = make_password(new_password)
        user.save()
        send_mail(
            'Восстановление пароля',
            'Ваш новый пароль: {}'.format(new_password),
            EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
        return redirect('login')
