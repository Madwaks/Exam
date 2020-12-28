from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.edit import View, FormView

from student.forms import StudentUserForm, StudentForm


class StudentSignup(FormView):
    template_name = "student/studentsignup.html"

    def get_context_data(self, **kwargs):
        userForm = StudentUserForm()
        studentForm = StudentForm()
        return {"userForm": userForm, "studentForm": studentForm}

    def post(self, request, *args, **kwargs):
        userForm = StudentUserForm(request.POST)
        studentForm = StudentForm(request.POST, request.FILES)
        if userForm.is_valid() and studentForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            student = studentForm.save(commit=False)
            student.user = user
            student.save()
            my_student_group = Group.objects.get_or_create(name="STUDENT")
            my_student_group[0].user_set.add(user)
        return HttpResponseRedirect("studentlogin")
