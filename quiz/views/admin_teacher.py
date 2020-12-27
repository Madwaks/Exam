from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render
from django.views import View

from teacher.models import Teacher


class AdminTeacher(View):
    @login_required(login_url="adminlogin")
    def get(self, request):
        dict = {
            "total_teacher": Teacher.objects.all().filter(status=True).count(),
            "pending_teacher": Teacher.objects.all().filter(status=False).count(),
            "salary": Teacher.objects.all()
            .filter(status=True)
            .aggregate(Sum("salary"))["salary__sum"],
        }
        return render(request, "quiz/admin_teacher.html", context=dict)
