from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    ForgetPasswordView,
    UserProfileView,
)

urlpatterns = [
    path("register", RegisterView.as_view()),
    path("login", LoginView.as_view()),
    path("resetpassword", ForgetPasswordView.as_view()),
]
