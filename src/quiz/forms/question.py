from django import forms
from django.forms import ModelForm

from quiz import models
from quiz.models import Question


class QuestionForm(ModelForm):

    # this will show dropdown __str__ method course model is shown on html so override it
    # to_field_name this will fetch corresponding value  user_id present in course model and return it
    courseID = forms.ModelChoiceField(
        queryset=models.Course.objects.all(),
        empty_label="Course Name",
        to_field_name="id",
    )

    def save(self, commit=True):
        question: Question = super(QuestionForm, self).save(commit=False)
        question.course = self.cleaned_data["courseID"]
        question.save()
        return question

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
