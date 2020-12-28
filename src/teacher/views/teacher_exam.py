from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from typing import Optional

from quiz.views.utils import is_teacher


@method_decorator(login_required, name="dispatch")
class TeacherExam(TemplateView, UserPassesTestMixin):
    template_name = "teacher/teacher_exam.html"

    def test_func(self) -> Optional[bool]:
        return is_teacher(self.request.user)
