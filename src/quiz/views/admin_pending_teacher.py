from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from teacher.models import Teacher


@method_decorator(login_required, name="dispatch")
class AdminPendingTeacher(ListView):
    template_name = "quiz/admin_view_pending_teacher.html"

    def get_queryset(self):
        return Teacher.objects.all().filter(status=False)
