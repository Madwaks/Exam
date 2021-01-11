from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.base import View

from quiz.models import Course, Question, Result
from quiz.views.utils import is_student
from student.models import Student


class Exams(LoginRequiredMixin, UserPassesTestMixin, ListView):
    login_url = "studentlogin"
    template_name = "student/student_exam.html"
    model = Course

    def test_func(self):
        return is_student(self.request.user)


class TakeExam(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "student/take_exam.html"
    login_url = "studentlogin"

    def test_func(self):
        return is_student(self.request.user)

    def get_context_data(self, **kwargs):
        course = Course.objects.get(id=kwargs.get("pk"))
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


class StartExam(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = "studentlogin"

    def test_func(self):
        return is_student(self.request.user)

    def get(self, request, pk):
        course = Course.objects.get(id=pk)
        questions = Question.objects.all().filter(course=course)
        response = render(
            request,
            "student/start_exam.html",
            {"course": course, "questions": questions},
        )
        response.set_cookie("course_id", course.id)
        return response


class CalculateMarks(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = "studentlogin"

    def test_func(self):
        return is_student(self.request.user)

    def get(self, request):
        if request.COOKIES.get("course_id") is not None:
            course_id = request.COOKIES.get("course_id")
            course = Course.objects.get(id=course_id)

            total_marks = 0
            questions = Question.objects.all().filter(course=course)
            for i in range(len(questions)):
                selected_ans = request.COOKIES.get(str(i + 1))
                actual_answer = questions[i].answer
                if selected_ans == actual_answer:
                    total_marks = total_marks + questions[i].marks
            student = Student.objects.get(user_id=request.user.id)
            result = Result()
            result.marks = total_marks
            result.exam = course
            result.student = student
            result.save()

            return HttpResponseRedirect("view-result")


class ResultView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    login_url = "studentlogin"
    model = Course
    template_name = "student/view_result.html"

    def test_func(self):
        return is_student(self.request.user)


class CheckMark(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    login_url = "studentlogin"
    template_name = "student/check_marks.html"

    def test_func(self):
        return is_student(self.request.user)

    def get_context_data(self, **kwargs):
        course = Course.objects.get(id=kwargs.get("pk"))
        student = Student.objects.get(user_id=self.request.user.id)
        results = Result.objects.all().filter(exam=course).filter(student=student)

        return {"results": results}


class StudentMark(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Course
    template_name = "student/student_marks.html"
    login_url = "studentlogin"

    def test_func(self):
        return is_student(self.request.user)
