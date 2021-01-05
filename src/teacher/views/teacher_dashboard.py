from typing import Dict, Any
from typing import Optional

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.base import TemplateView

from quiz.models import Course, Question
from student.models import Student


def is_teacher(user):
    return user.groups.filter(name="TEACHER").exists()


class TeacherDashboard(TemplateView, UserPassesTestMixin, LoginRequiredMixin):
    template_name = "teacher/teacher_dashboard.html"
    login_url = "teacherlogin"

    def test_func(self) -> Optional[bool]:
        return is_teacher(self.request.user)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = {
            "total_course": Course.objects.all().count(),
            "total_question": Question.objects.all().count(),
            "total_student": Student.objects.all().count(),
        }
        return context
