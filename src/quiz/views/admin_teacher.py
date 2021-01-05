from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from teacher.models import Teacher


@method_decorator(login_required, name="dispatch")
class AdminTeacher(TemplateView):
    template_name = "quiz/admin_teacher.html"

    def get(self, request, *args, **kwargs):
        context = {
            "total_teacher": Teacher.objects.all().filter(status=True).count(),
            "pending_teacher": Teacher.objects.all().filter(status=False).count(),
        }
        return render(self.request, self.template_name, context=context)


@method_decorator(login_required, name="dispatch")
class AdminView(TemplateView):
    template_name = "quiz/admin_view_teacher.html"

    def get(self, request, *args, **kwargs):
        teachers = Teacher.objects.all().filter(status=True)
        return render(self.request, self.template_name, {"teachers": teachers})
