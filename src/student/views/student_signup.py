from django.contrib.auth.models import Group, User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from student.forms import StudentUserForm
from student.models import Student


class StudentSignup(CreateView):
    template_name = "student/studentsignup.html"
    form_class = StudentUserForm
    success_url = reverse_lazy("/student/studentlogin")
    model = Student

    # def form_valid(self, form):
    #     breakpoint()
    #     user = User(username=self.request.POST.get("username"))
    #     user.set_password(self.request.POST.get("password"))
    #     user.save()
    #     teacher_group = Group.objects.get_or_create(name="STUDENT")
    #     teacher_group[0].user_set.add(user)
    #     teacher = Student(user=user)
    #     teacher.save()
    #     return HttpResponseRedirect("studentlogin")
