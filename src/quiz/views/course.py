from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView

from quiz.forms.course import CourseForm
from quiz.models import Course


class CourseView(TemplateView, LoginRequiredMixin):
    template_name = "quiz/admin_course.html"
    login_url = "adminlogin"


class AddCourse(CreateView, LoginRequiredMixin):
    login_url = "adminlogin"
    form_class = CourseForm
    model = Course
    template_name = "quiz/admin_add_course.html"
    success_url = reverse_lazy("admin-view-course")


class CourseListView(ListView, LoginRequiredMixin):
    login_url = "adminlogin"
    template_name = "quiz/admin_view_course.html"
    model = Course


class DeleteCourse(DeleteView, LoginRequiredMixin):
    model = Course
    template_name = "quiz/course_confirm_delete.html"
    success_url = reverse_lazy("admin-view-course")
    login_url = "adminlogin"
