from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView

from quiz.forms.course import CourseForm
from quiz.models import Course
from quiz.views.utils import is_teacher


class TeacherAddExam(CreateView, UserPassesTestMixin, LoginRequiredMixin):
    login_url = "adminlogin"
    model = Course
    form_class = CourseForm
    template_name = "teacher/teacher_add_exam.html"

    def test_func(self):
        return is_teacher(self.request.user)

    def get_success_url(self):
        return reverse("/teacher/teacher-view-exam")
