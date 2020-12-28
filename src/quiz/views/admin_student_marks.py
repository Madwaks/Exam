from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

from quiz.models import Course, Result
from student.models import Student


class AdminStudentMarks(TemplateView, LoginRequiredMixin):
    login_url = "adminlogin"
    template_name = "quiz/admin_view_student_marks.html"

    def get_context_data(self, **kwargs):
        return {"students": Student.objects.all()}


class AdminStudentMarksView(TemplateView, LoginRequiredMixin):
    login_url = "adminlogin"
    template_name = "quiz/admin_view_marks.html"

    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        response = render(request, "quiz/admin_view_marks.html", {"courses": courses})
        response.set_cookie("student_id", str(kwargs.get("pk")))
        return response


class AdminCheckMarks(TemplateView, LoginRequiredMixin):
    login_url = "adminlogin"
    template_name = "quiz/admin_check_marks.html"

    def get_context_data(self, **kwargs):
        course = Course.objects.get(id=kwargs.get("pk"))
        student_id = self.request.COOKIES.get("student_id")
        student = Student.objects.get(id=student_id)

        results = Result.objects.all().filter(exam=course).filter(student=student)
        return {"results": results}
