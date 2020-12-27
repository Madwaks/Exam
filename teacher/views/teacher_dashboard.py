from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from student.models import Student
from quiz.models import Question
from quiz.models import Course
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from typing import Optional
from typing import Dict, Any

def is_teacher(user):
    return user.groups.filter(name="TEACHER").exists()

@method_decorator(login_required, name="dispatch")
class TeacherDashboard(TemplateView, UserPassesTestMixin):
    template_name = "teacher/teacher_dashboard.html"

    def test_func(self) -> Optional[bool]:
        return is_teacher(self.request.user)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = {
        "total_course": Course.objects.all().count(),
        "total_question": Question.objects.all().count(),
        "total_student": Student.objects.all().count(),
    }
        return context



# def teacher_dashboard_view(request):
#     dict = {
#         "total_course": QMODEL.Course.objects.all().count(),
#         "total_question": QMODEL.Question.objects.all().count(),
#         "total_student": SMODEL.Student.objects.all().count(),
#     }
#     return render(request, self.template_name, context=dict)
