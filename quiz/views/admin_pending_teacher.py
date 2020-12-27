from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from teacher.models import Teacher


@method_decorator(login_required, name="dispatch")
class AdminPendingTeacher(TemplateView):
    template_name = "quiz/admin_view_pending_teacher.html"

    def get(self, request, *args, **kwargs):
        teachers = Teacher.objects.all().filter(status=False)
        return render(self.request, self.template_name, context={"teachers": teachers})
