from django.contrib.auth.views import LoginView


class TeacherLogin(LoginView):
    template_name = "teacher/teacherlogin.html"
