from django.db import models

from quiz.models.course import Course


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    question = models.CharField(max_length=600)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    cat = (
        ("Option1", "Option1"),
        ("Option2", "Option2"),
        ("Option3", "Option3"),
        ("Option4", "Option4"),
    )
    answer = models.CharField(max_length=200, choices=cat)

    def __str__(self):
        return str(self.question)
