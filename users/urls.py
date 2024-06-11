from django.contrib.auth.views import LoginView
from django.urls import path
from users.apps import UsersConfig
from users.views import CustomLogoutView, RegisterView, ProfileView, VerifyEmailView, PasswordResetView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("verify/<int:pk>/", VerifyEmailView.as_view(), name="verify"),
    path("reset_password/", PasswordResetView.as_view(), name="reset_password"),

]
