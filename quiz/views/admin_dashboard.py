from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View

from quiz.models import Question, Course
from student.models import Student
from teacher.models import Teacher


class AdminDashboard(View):
    @login_required(login_url="adminlogin")
    def get(self, request):
        dict = {
            "total_student": Student.objects.all().count(),
            "total_teacher": Teacher.objects.all().filter(status=True).count(),
            "total_course": Course.objects.all().count(),
            "total_question": Question.objects.all().count(),
        }
        return render(request, "quiz/admin_dashboard.html", context=dict)
