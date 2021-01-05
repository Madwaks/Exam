from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView

from quiz.forms.question import QuestionForm
from quiz.models import Course, Question
from quiz.views.utils import is_teacher


class QuestionView(TemplateView, LoginRequiredMixin):
    login_url = "teacherlogin"
    template_name = "teacher/teacher_question.html"


class QuestionList(ListView, UserPassesTestMixin, LoginRequiredMixin):
    model = Course
    template_name = "teacher/teacher_view_question.html"

    def test_func(self):
        return is_teacher(self.request.user)


class AddQuestion(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    login_url = "teacherlogin"
    success_url = reverse_lazy("teacher-view-question")
    template_name = "teacher/teacher_add_question.html"
    form_class = QuestionForm
    model = Question

    def test_func(self):
        return is_teacher(self.request.user)


class DetailQuestions(TemplateView, LoginRequiredMixin, UserPassesTestMixin):
    template_name = "teacher/see_question.html"
    login_url = "teacherlogin"

    def test_func(self):
        return is_teacher(self.request.user)

    def get_context_data(self, **kwargs):
        return {"questions": Question.objects.all().filter(course_id=kwargs.get("pk"))}


class DeleteQuestion(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    login_url = "teacherlogin"
    success_url = reverse_lazy("teacher-view-question")
    model = Question
    template_name = "quiz/course_confirm_delete.html"

    def test_func(self):
        return is_teacher(self.request.user)
