from django.http import HttpResponseRedirect
from django.views import View


class AdminClick(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect("afterlogin")
        return HttpResponseRedirect("adminlogin")
