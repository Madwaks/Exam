from django.views.generic.base import TemplateView


class AboutUsView(TemplateView):
    template_name = "quiz/aboutus.html"
