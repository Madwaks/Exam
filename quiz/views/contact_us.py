from django.core.mail import send_mail
from django.shortcuts import render
from django.views import View

from onlinequiz import settings
from quiz.forms.contact_us import ContactusForm


class ContactUsView(View):
    def get(self, request):
        sub = ContactusForm()
        if request.method == "POST":
            sub = ContactusForm(request.POST)
            if sub.is_valid():
                email = sub.cleaned_data["Email"]
                name = sub.cleaned_data["Name"]
                message = sub.cleaned_data["Message"]
                send_mail(
                    str(name) + " || " + str(email),
                    message,
                    settings.EMAIL_HOST_USER,
                    settings.EMAIL_RECEIVING_USER,
                    fail_silently=False,
                )
                return render(request, "quiz/contactussuccess.html")
        return render(request, "quiz/contactus.html", {"form": sub})
