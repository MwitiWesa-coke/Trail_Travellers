from django.urls import path
from . import views

urlpatterns = [
    path("login-page/", views.login_page, name="login_page"),
    path("register-page/", views.register_page, name="register_page"),

    path("register/", views.register_view, name="register"),

    path("login/", views.login_view, name="login"),
    path("profile/", views.profile_view, name="profile"),
    path("drivers/", views.driver_list, name="drivel-list"),
]