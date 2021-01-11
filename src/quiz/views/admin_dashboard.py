from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from quiz.models import Course, Question
from student.models import Student
from teacher.models import Teacher


class AdminDashboard(LoginRequiredMixin, TemplateView):
    template_name = "quiz/admin_dashboard.html"
    login_url = "adminlogin"

    def get_context_data(self, **kwargs):
        context = {
            "total_student": Student.objects.all().count(),
            "total_teacher": Teacher.objects.all().filter(status=True).count(),
            "total_course": Course.objects.all().count(),
            "total_question": Question.objects.all().count(),
        }
        return context
