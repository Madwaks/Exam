from django.urls import path

from teacher.views.exam import TeacherAddExam, ExamView, DeleteExam
from teacher.views.login import TeacherLogin
from teacher.views.question import (
    QuestionView,
    AddQuestion,
    QuestionList,
    DetailQuestions,
    DeleteQuestion,
)
from teacher.views.signup import Signup
from teacher.views.teacher_click import TeacherClick
from teacher.views.teacher_dashboard import TeacherDashboard
from teacher.views.teacher_exam import TeacherExam

urlpatterns = [
    path("teacherclick", TeacherClick.as_view()),
    path("teacherlogin", TeacherLogin.as_view(), name="teacherlogin"),
    path("teachersignup", Signup.as_view(), name="teachersignup"),
    path("teacher-dashboard", TeacherDashboard.as_view(), name="teacher-dashboard"),
    path("teacher-exam", TeacherExam.as_view(), name="teacher-exam"),
    path("teacher-add-exam", TeacherAddExam.as_view(), name="teacher-add-exam"),
    path("teacher-view-exam", ExamView.as_view(), name="teacher-view-exam"),
    path("delete-exam/<int:pk>", DeleteExam.as_view(), name="delete-exam"),
    path("teacher-question", QuestionView.as_view(), name="teacher-question"),
    path("teacher-add-question", AddQuestion.as_view(), name="teacher-add-question"),
    path("teacher-view-question", QuestionList.as_view(), name="teacher-view-question"),
    path("see-question/<int:pk>", DetailQuestions.as_view(), name="see-question"),
    path("remove-question/<int:pk>", DeleteQuestion.as_view(), name="remove-question"),
]
