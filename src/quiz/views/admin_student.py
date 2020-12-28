from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, FormView

from student.forms import StudentForm, StudentUserForm
from student.models import Student


class AdminStudent(TemplateView, LoginRequiredMixin):
    login_url = "adminlogin"
    template_name = "quiz/admin_student.html"
    model = Student

    def get_context_data(self, **kwargs):
        return {"total_student": Student.objects.all().count()}


class AdminStudentView(ListView, LoginRequiredMixin):
    login_url = "adminlogin"
    template_name = "quiz/admin_view_student.html"
    model = Student

    def get_context_data(self, **kwargs):
        return {"students": Student.objects.all()}


# @login_required(login_url="adminlogin")
# def update_student_view(request, pk):
#     student = SMODEL.Student.objects.get(id=pk)
#     user = SMODEL.User.objects.get(id=student.user_id)
#     userForm = SFORM.StudentUserForm(instance=user)
#     studentForm = SFORM.StudentForm(request.FILES, instance=student)
#     mydict = {"userForm": userForm, "studentForm": studentForm}
#     if request.method == "POST":
#         userForm = SFORM.StudentUserForm(request.POST, instance=user)
#         studentForm = SFORM.StudentForm(request.POST, request.FILES, instance=student)
#         if userForm.is_valid() and studentForm.is_valid():
#             user = userForm.save()
#             user.set_password(user.password)
#             user.save()
#             studentForm.save()
#             return redirect("admin-view-student")
#     return render(request, "quiz/update_student.html", context=mydict)
#
class UpdateStudent(FormView, LoginRequiredMixin):
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
