from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import FormView

from onlinequiz import settings
from quiz.forms.contact_us import ContactusForm


class ContactUsView(FormView):
    template_name = "quiz/contactus.html"

    def get_form(self, form_class=None):
        sub = ContactusForm()
        return sub

    def post(self, request, *args, **kwargs):
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
