from django import forms


class TeacherSalaryForm(forms.Form):
    salary = forms.IntegerField()
