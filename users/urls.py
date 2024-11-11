from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("", views.Users.as_view()),
    path("me", views.Me.as_view()),
    path("change-password", views.ChangePassword.as_view()),
    # 쿠키
    path("log-in", views.LogIn.as_view()),
    path("log-out", views.LogOut.as_view()),
    # 토큰 로그인
    path("token-login", obtain_auth_token),
    # jwt 로그인
    path("jwt-login", views.JWTLogin.as_view()),
    path("@<str:username>", views.PublicUser.as_view()),
]
