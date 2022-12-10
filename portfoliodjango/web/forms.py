from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class USerRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contrasenia", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirma Contrasenia", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields }
