from django import forms

from quiz import models


class QuestionForm(forms.ModelForm):

    # this will show dropdown __str__ method course model is shown on html so override it
    # to_field_name this will fetch corresponding value  user_id present in course model and return it
    courseID = forms.ModelChoiceField(
        queryset=models.Course.objects.all(),
        empty_label="Course Name",
        to_field_name="id",
    )

    class Meta:
        model = models.Question
        fields = [
            "marks",
            "question",
            "option1",
            "option2",
            "option3",
            "option4",
            "answer",
        ]
        widgets = {"question": forms.Textarea(attrs={"rows": 3, "cols": 50})}
