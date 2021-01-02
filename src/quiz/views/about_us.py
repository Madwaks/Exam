from django.views.generic.base import View, TemplateView


class AboutUsView(TemplateView):
    template_name = "quiz/aboutus.html"
