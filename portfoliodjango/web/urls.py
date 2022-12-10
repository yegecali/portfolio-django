from django.urls import path
from .views import page_index, page_admin, page_sign_in, page_register
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path("", page_index, name="index"),
    path("sign-in/", LoginView.as_view(template_name="sign-in.html"), name="signin"),
    path("register/", page_register, name="register"),
    path("admin/", page_admin, name="admin"),
]