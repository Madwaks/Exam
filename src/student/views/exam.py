from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from quiz.models import Course, Question
from quiz.views.utils import is_student


class Exams(ListView, LoginRequiredMixin, UserPassesTestMixin):
    login_url = "studentlogin"
    template_name = "student/student_exam.html"
    model = Course

    def test_func(self):
        return is_student(self.request.user)


class TakeExam(TemplateView, UserPassesTestMixin, LoginRequiredMixin):
    template_name = "student/take_exam.html"
    login_url = "studentlogin"

    def test_func(self):
        return is_student(self.request.user)

    def get_context_data(self, **kwargs):
        course = Course.objects.get(id=pk)
        total_questions = Question.objects.all().filter(course=course).count()
        questions = Question.objects.all().filter(course=course)
        total_marks = 0
        for q in questions:
            total_marks = total_marks + q.marks

        return {
            "course": course,
            "total_questions": total_questions,
            "total_marks": total_marks,
        }


@login_required(login_url="studentlogin")
@user_passes_test(is_student)
def start_exam_view(request, pk):
    course = Course.objects.get(id=pk)
    questions = Question.objects.all().filter(course=course)
    if request.method == "POST":
        pass
    response = render(
        request, "student/start_exam.html", {"course": course, "questions": questions}
    )
    response.set_cookie("course_id", course.id)
    return response
