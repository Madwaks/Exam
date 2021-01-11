from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView

from quiz.models import Course, Question
from quiz.views.utils import is_student


class DashBoard(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    login_url = "studentlogin"
    template_name = "student/student_dashboard.html"

    def test_func(self):
        return is_student(self.request.user)

    def get_context_data(self, **kwargs):
        return {
            "total_course": Course.objects.all().count(),
            "total_question": Question.objects.all().count(),
        }
