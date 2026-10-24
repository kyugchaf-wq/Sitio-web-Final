from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Correo electrónico"
    )

    first_name = forms.CharField(
        max_length=150,
        required=True,
        label="Nombre"
    )

    last_name = forms.CharField(
        max_length=150,
        required=True,
        label="Apellido"
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]