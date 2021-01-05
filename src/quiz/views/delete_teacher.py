from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
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
