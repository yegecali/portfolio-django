from django.urls import path
from .views import page_index, page_admin, page_sign_in, page_register
urlpatterns = [
    path("", page_index, name="index"),
    path("auth/sign-in/", page_sign_in, name="signin"),
    path("auth/register/", page_register, name="register"),
    path("admin/", page_admin, name="admin")
]