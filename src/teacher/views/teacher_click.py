from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View


class TeacherClick(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect("afterlogin")
        return render(request, "teacher/teacherclick.html")
