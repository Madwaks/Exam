from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from teacher.models import Teacher


@method_decorator(login_required, name="dispatch")
class ApproveTeacher(UpdateView):
    model = Teacher

    def post(self, request, *args, **kwargs):
        teacher = Teacher.objects.get(id=kwargs.get("pk"))
        teacher.status = True
        teacher.save()
        return HttpResponseRedirect("/admin-view-pending-teacher")
