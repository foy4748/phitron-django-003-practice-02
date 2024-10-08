from django.urls import path
from . import views

app_name = "auth"

urlpatterns = [
    # For Django Hard Reload
    path("register/", views.ShowRegistrationForm, name="registration_form"),
    path("login/", views.ShowLoginForm, name="login_form"),
    path("logout/", views.LogoutUser, name="logout"),
]
