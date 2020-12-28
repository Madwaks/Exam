from django.contrib.auth.views import LoginView
from django.urls import path

from student.views.dashboard import DashBoard
from student.views.exam import Exams, TakeExam, start_exam_view
from student.views.student_click import StudentClick
from student.views.student_signup import StudentSignup


urlpatterns = [
    path("studentclick", StudentClick.as_view()),
    path(
        "studentlogin",
        LoginView.as_view(template_name="student/studentlogin.html"),
        name="studentlogin",
    ),
    path("studentsignup", StudentSignup.as_view(), name="studentsignup"),
    path("student-dashboard", DashBoard.as_view(), name="student-dashboard"),
    path("student-exam", Exams.as_view(), name="student-exam"),
    path("take-exam/<int:pk>", TakeExam.as_view(), name="take-exam"),
    path("start-exam/<int:pk>", start_exam_view, name="start-exam"),
    # path("calculate-marks", views.calculate_marks_view, name="calculate-marks"),
    # path("view-result", views.view_result_view, name="view-result"),
    # path("check-marks/<int:pk>", views.check_marks_view, name="check-marks"),
    # path("student-marks", views.student_marks_view, name="student-marks"),
]
