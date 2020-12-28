from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView

from teacher.forms import TeacherForm, TeacherUserForm


class Signup(FormView):
    template_name = "teacher/teachersignup.html"

    def get_context_data(self, **kwargs):
        userForm = TeacherUserForm()
        teacherForm = TeacherForm()
        return {"userForm": userForm, "teacherForm": teacherForm}

    def post(self, request, *args, **kwargs):
        user_form = TeacherUserForm(request.POST)
        teacher_form = TeacherForm(request.POST, request.FILES)
        if user_form.is_valid() and teacher_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            teacher = teacher_form.save(commit=False)
            teacher.user = user
            teacher.save()
            my_teacher_group = Group.objects.get_or_create(name="TEACHER")
            my_teacher_group[0].user_set.add(user)
        return HttpResponseRedirect("teacherlogin")
