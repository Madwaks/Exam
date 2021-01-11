from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views import View

from teacher.models import Teacher


class ApproveTeacher(LoginRequiredMixin, View):
    model = Teacher
    fields = ["status"]
    login_url = "adminlogin"

    def get(self, *args, **kwargs):
        teacher = Teacher.objects.get(id=kwargs.get("pk"))
        teacher.status = True
        teacher.save()
        return HttpResponseRedirect("/admin-view-pending-teacher")
