from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from teacher.models import Teacher


class UpdateTeacher(UpdateView, LoginRequiredMixin):
    login_url = "adminlogin"
    template_name = "quiz/update_teacher.html"
    model = Teacher
    fields = ["user"]
