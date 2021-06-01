from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


app_name = "users"
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name = "login_view"),
    path("register/", views.register_view, name = "register_view"),


]