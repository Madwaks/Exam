from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from teacher.forms import TeacherUserForm, TeacherForm
from teacher.models import Teacher


class UpdateTeacher(UpdateView, LoginRequiredMixin):
    login_url = "adminlogin"
    template_name = "quiz/update_teacher.html"
    model = Teacher
    fields = ["user"]

    def post(self, request, *args, **kwargs):
        teacher = Teacher.objects.get(id=kwargs.get("pk"))
        user = User.objects.get(id=teacher.user_id)
        userForm = TeacherUserForm(instance=user)
        teacherForm = TeacherForm(request.FILES, instance=teacher)
        context = {"userForm": userForm, "teacherForm": teacherForm}
        userForm = TeacherUserForm(request.POST, instance=user)
        teacherForm = TeacherForm(request.POST, request.FILES, instance=teacher)
        if userForm.is_valid() and teacherForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            teacherForm.save()
            return redirect("admin-view-teacher")
        return render(request, self.template_name, context=context)
