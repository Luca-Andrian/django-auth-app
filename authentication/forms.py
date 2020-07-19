# -*- encoding: utf-8 -*-

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        initial="",
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",
                # "class": "form-control"
            }
        )
    )
    email = forms.EmailField(
        initial="",
        required=False,
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",
                # "class": "form-control"
            }
        ),
    )
    password = forms.CharField(
        initial="",
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",
                "class": "form-control"
            }
        )
    )

#EOF
