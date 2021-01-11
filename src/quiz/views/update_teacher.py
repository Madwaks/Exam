from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from teacher.forms.teacher import TeacherUserForm
from teacher.models import Teacher


class UpdateTeacher(LoginRequiredMixin, UpdateView):
    login_url = "adminlogin"
    template_name = "quiz/update_teacher.html"
    model = Teacher
    form_class = TeacherUserForm
    success_url = reverse_lazy("admin-view-teacher")
