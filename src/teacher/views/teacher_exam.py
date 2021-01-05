from typing import Optional

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.base import TemplateView

from quiz.views.utils import is_teacher


class TeacherExam(TemplateView, UserPassesTestMixin, LoginRequiredMixin):
    template_name = "teacher/teacher_exam.html"
    login_url = "teacherlogin"

    def test_func(self) -> Optional[bool]:
        return is_teacher(self.request.user)
