from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


app_name = "users"
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name = "login_view"),
    path("register/", views.register_view, name = "register_view"),
    path("logout/", views.logout_view, name = "logout_view"),
    path("u/<str:username>/", views.profile_view, name = "profile_view"),
    path("follow_unfollow/<str:username>/", views.follow_unfollow, name = "follow_unfollow"),
    # path("settings/up_edit/", views.user_edit_view, name = "user_edit"),

]