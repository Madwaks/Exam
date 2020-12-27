from django import forms

from quiz import models


class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ["course_name", "question_number", "total_marks"]
