from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView


class StudentClick(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect("afterlogin")
        return render(request, "student/studentclick.html")
