from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    DetailView,
    DeleteView,
)

from quiz.forms.question import QuestionForm
from quiz.models import Question


class QuestionView(TemplateView, LoginRequiredMixin):
    login_url = "adminlogin"
    template_name = "quiz/admin_question.html"


class AddQuestion(CreateView, LoginRequiredMixin):
    login_url = "adminlogin"
    form_class = QuestionForm
    model = Question
    template_name = "quiz/admin_add_question.html"
    success_url = reverse_lazy("admin-view-question")


class QuestionListView(ListView, LoginRequiredMixin):
    login_url = "adminlogin"
    model = Question
    template_name = "quiz/admin_view_question.html"


class ViewQuestion(DetailView, LoginRequiredMixin):
    login_url = "adminlogin"
    model = Question
    template_name = "quiz/view_question.html"


class DeleteQuestion(DeleteView, LoginRequiredMixin):
    login_url = "adminlogin"
    model = Question
    success_url = reverse_lazy("admin-view-question")
    template_name = "quiz/course_confirm_delete.html"
