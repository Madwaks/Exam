from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, DeleteView

from student.forms import StudentUserForm
from student.models import Student


class AdminStudent(LoginRequiredMixin, TemplateView):
    login_url = "adminlogin"
    template_name = "quiz/admin_student.html"
    model = Student

    def get_context_data(self, **kwargs):
        return {"total_student": Student.objects.all().count()}


class AdminStudentView(LoginRequiredMixin, ListView):
    login_url = "adminlogin"
    template_name = "quiz/admin_view_student.html"
    model = Student


class AdminDeleteStudent(LoginRequiredMixin, DeleteView):
    model = Student
    login_url = "adminlogin"
    template_name = "quiz/course_confirm_delete.html"
    success_url = reverse_lazy("admin-view-student")


class UpdateStudent(LoginRequiredMixin, FormView):
    login_url = "adminlogin"

    def get_context_data(self, **kwargs):
        student = Student.objects.get(id=kwargs.get("pk"))
        user = User.objects.get(id=student.user_id)
        userForm = StudentUserForm(instance=user)
        studentForm = StudentForm(self.request.FILES, instance=student)
        return {"userForm": userForm, "studentForm": studentForm}

    def post(self, request, *args, **kwargs):
        student = Student.objects.get(id=kwargs.get("pk"))
        userForm = StudentUserForm(request.POST, instance=self.request.user)
        studentForm = StudentForm(request.POST, request.FILES, instance=student)
        if userForm.is_valid() and studentForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            studentForm.save()
            return redirect("admin-view-student")
