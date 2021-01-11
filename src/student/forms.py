from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from student.models import Student


class StudentUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        widgets = {"password": forms.PasswordInput()}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        teacher_group = Group.objects.get_or_create(name="STUDENT")
        teacher_group[0].user_set.add(user)
        student = Student(user=user)
        student.save()
        if commit:
            student.save()
        return student
