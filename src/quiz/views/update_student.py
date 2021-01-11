# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy
# from django.views.generic import UpdateView
#
#
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
#
# class UpdateStudent(LoginRequiredMixin, UpdateView):
#     template_name = "quiz/update_student.html"
#     success_url = reverse_lazy("admin-view-student")
#     form_class =
