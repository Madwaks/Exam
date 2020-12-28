from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect

# for showing signup/login button for teacher


class TeacherClick(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect("afterlogin")
        return render(request, "teacher/teacherclick.html")


# def teacherclick_view(request):
#     if request.user.is_authenticated:
#         return HttpResponseRedirect("afterlogin")
#     return render(request, "teacher/teacherclick.html")
