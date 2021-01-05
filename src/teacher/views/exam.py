from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView

from quiz.forms.course import CourseForm
from quiz.models import Course
from quiz.views.utils import is_teacher


class TeacherAddExam(CreateView, UserPassesTestMixin, LoginRequiredMixin):
    model = Course
    form_class = CourseForm
    template_name = "teacher/teacher_add_exam.html"
    login_url = "teacherlogin"
    success_url = "/teacher/teacher-view-exam"

    def test_func(self):
        return is_teacher(self.request.user)


class ExamView(ListView, UserPassesTestMixin, LoginRequiredMixin):
    login_url = "teacherlogin"
    model = Course
    template_name = "teacher/teacher_view_exam.html"

    def test_func(self):
        return is_teacher(self.request.user)


class DeleteExam(DeleteView, UserPassesTestMixin, LoginRequiredMixin):
    login_url = "teacherlogin"
    success_url = reverse_lazy("teacher-view-exam")
    model = Course

    def test_func(self):
        return is_teacher(self.request.user)
