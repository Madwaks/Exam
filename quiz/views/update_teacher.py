from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from teacher.forms import TeacherForm, TeacherUserForm
from teacher.models import Teacher


class UpdateTeacher(TemplateView):
    template_name = "quiz/update_teacher.html"

    @login_required(login_url="adminlogin")
    def post(self, request, pk):
        breakpoint()
        teacher = Teacher.objects.get(id=pk)
        user = User.objects.get(id=teacher.user_id)
        userForm = TeacherUserForm(instance=user)
        teacherForm = TeacherForm(request.FILES, instance=teacher)
        mydict = {"userForm": userForm, "teacherForm": teacherForm}
        userForm = TeacherUserForm(request.POST, instance=user)
        teacherForm = TeacherForm(request.POST, request.FILES, instance=teacher)
        if userForm.is_valid() and teacherForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            teacherForm.save()
            return redirect("admin-view-teacher")
        return render(request, self.template_name, context=mydict)
