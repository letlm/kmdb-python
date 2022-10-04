from django.urls import path

from . import views

urlpatterns = [
    path("users/register/", views.UserRegisterView.as_view()),
    path("users/login/", views.LoginView.as_view()),
    path("users/", views.UserView.as_view()),
    path("users/<int:user_id>/", views.UserDetaislView.as_view()),
]
