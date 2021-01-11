from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from teacher.models import Teacher


class AdminPendingTeacher(LoginRequiredMixin, ListView):
    template_name = "quiz/admin_view_pending_teacher.html"

    def get_queryset(self):
        return Teacher.objects.all().filter(status=False)
