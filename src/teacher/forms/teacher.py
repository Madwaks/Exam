from django.contrib.auth.models import User
from django.forms import ModelForm, PasswordInput


class TeacherUserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {"password": PasswordInput()}

    def save(self, commit=True):
        breakpoint()
