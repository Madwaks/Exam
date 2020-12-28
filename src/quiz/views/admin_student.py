from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView

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
# class UpdateStudent(UpdateView, LoginRequiredMixin):
#     login_url = "adminlogin"
#     model = Student
#     form_class =
