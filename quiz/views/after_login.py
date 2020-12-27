from django.shortcuts import redirect, render
from django.views import View

from quiz.views.utils import is_student, is_teacher
from teacher.models import Teacher


class AfterLogin(View):
    name = ""

    def get(self, request):
        if is_student(request.user):
            return redirect("student/student-dashboard")

        elif is_teacher(request.user):
            accountapproval = Teacher.objects.all().filter(
                user_id=request.user.id, status=True
            )
            if accountapproval:
                return redirect("teacher/teacher-dashboard")
            else:
                return render(request, "teacher/teacher_wait_for_approval.html")
        else:
            return redirect("admin-dashboard")
