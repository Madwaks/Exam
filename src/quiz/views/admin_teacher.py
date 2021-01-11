from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView

from teacher.models import Teacher


class AdminTeacher(LoginRequiredMixin, TemplateView):
    template_name = "quiz/admin_teacher.html"
    login_url = "adminlogin"

    def get_context_data(self, **kwargs):
        return {
            "total_teacher": Teacher.objects.all().filter(status=True).count(),
            "pending_teacher": Teacher.objects.all().filter(status=False).count(),
        }


class AdminView(LoginRequiredMixin, ListView):
    template_name = "quiz/admin_view_teacher.html"
    login_url = "adminlogin"

    def get_queryset(self):
        return Teacher.objects.all().filter(status=True)
