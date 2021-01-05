from django.contrib.auth.models import Group, User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView

from teacher.forms.teacher import TeacherUserForm
from teacher.models import Teacher


class Signup(CreateView):
    template_name = "teacher/teachersignup.html"
    form_class = TeacherUserForm
    success_url = reverse_lazy("/teacher/teacherlogin")
    model = Teacher

    def form_valid(self, form):
        user = User(username=self.request.POST.get("username"))
        user.set_password(self.request.POST.get("password"))
        user.save()
        teacher_group = Group.objects.get_or_create(name="TEACHER")
        teacher_group[0].user_set.add(user)
        teacher = Teacher(user=user)
        teacher.save()
        return HttpResponseRedirect("teacherlogin")
