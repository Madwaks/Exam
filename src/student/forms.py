from django import forms
from django.contrib.auth.models import User


class StudentUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {"password": forms.PasswordInput()}
