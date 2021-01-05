from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView

from teacher.models import Teacher


class DeleteTeacher(DeleteView, LoginRequiredMixin):
    model = Teacher
    login_url = "adminlogin"
    template_name = "quiz/course_confirm_delete.html"
    success_url = reverse_lazy("admin-view-teacher")


class RejectTeacher(DeleteView, LoginRequiredMixin):
    model = Teacher
    login_url = "adminlogin"
    template_name = "quiz/course_confirm_delete.html"
    success_url = reverse_lazy("admin-view-teacher")
