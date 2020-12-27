from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from teacher.models import Teacher


class AdminTeacher(TemplateView):
    template_name = "quiz/admin_teacher.html"

    @login_required(login_url="adminlogin")
    def get(self, request):
        context = {
            "total_teacher": Teacher.objects.all().filter(status=True).count(),
            "pending_teacher": Teacher.objects.all().filter(status=False).count(),
            "salary": Teacher.objects.all()
            .filter(status=True)
            .aggregate(Sum("salary"))["salary__sum"],
        }
        return render(request, self.template_name, context=context)


class AdminView(View):
    @login_required(login_url="adminlogin")
    def get(self, request):
        teachers = Teacher.objects.all().filter(status=True)
        return render(request, "quiz/admin_view_teacher.html", {"teachers": teachers})
