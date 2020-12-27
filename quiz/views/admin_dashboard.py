from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView

from quiz.models import Question, Course
from student.models import Student
from teacher.models import Teacher


@method_decorator(login_required, name="dispatch")
class AdminDashboard(TemplateView):
    def get_context_data(self, **kwargs):
        context = {
            "total_student": Student.objects.all().count(),
            "total_teacher": Teacher.objects.all().filter(status=True).count(),
            "total_course": Course.objects.all().count(),
            "total_question": Question.objects.all().count(),
        }
        return render(self.request, "quiz/admin_dashboard.html", context=context)
