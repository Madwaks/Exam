from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render

from django.views import View


class HomeView(View):
    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            return HttpResponseRedirect("afterlogin")
        return render(request, "quiz/index.html")
