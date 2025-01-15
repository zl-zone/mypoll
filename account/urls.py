# account/urls.py
from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path("create", views.create, name="create"),
    path("login", views.user_login, name="login"),
    path("logout", views.user_logout, name="logout"),
]