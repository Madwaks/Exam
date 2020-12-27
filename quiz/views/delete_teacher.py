from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView

from teacher.models import Teacher


@method_decorator(login_required, name="dispatch")
class DeleteTeacher(DeleteView):
    model = Teacher

    def delete(self, request, *args, **kwargs):
        teacher = Teacher.objects.get(id=kwargs.get("pk"))
        user = User.objects.get(id=teacher.user_id)
        user.delete()
        teacher.delete()
        return HttpResponseRedirect("/admin-view-teacher")


@method_decorator(login_required, name="dispatch")
class RejectTeacher(DeleteView):
    model = Teacher

    def post(self, request, *args, **kwargs):
        teacher = Teacher.objects.get(id=kwargs.get("pk"))
        user = User.objects.get(id=teacher.user_id)
        user.delete()
        teacher.delete()
        return HttpResponseRedirect("/admin-view-pending-teacher")
