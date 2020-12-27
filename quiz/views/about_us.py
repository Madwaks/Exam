from django.shortcuts import render
from django.views.generic.base import View


class AboutUsView(View):
    def get(self, request):
        return render(request, "quiz/aboutus.html")
