import debug_toolbar
from django.contrib import admin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include

from quiz.views.about_us import AboutUsView
from quiz.views.admin_click import AdminClick
from quiz.views.admin_dashboard import AdminDashboard
from quiz.views.admin_pending_teacher import AdminPendingTeacher
from quiz.views.admin_student import (
    AdminStudent,
    AdminStudentView,
    UpdateStudent,
    AdminDeleteStudent,
)
from quiz.views.admin_student_marks import (
    AdminStudentMarks,
    AdminStudentMarksView,
    AdminCheckMarks,
)
from quiz.views.admin_teacher import AdminTeacher, AdminView
from quiz.views.after_login import AfterLogin
from quiz.views.approve_teacher import ApproveTeacher
from quiz.views.course import CourseView, AddCourse, CourseListView, DeleteCourse
from quiz.views.delete_teacher import DeleteTeacher, RejectTeacher
from quiz.views.home import HomeView
from quiz.views.question import (
    AddQuestion,
    QuestionListView,
    QuestionView,
    ViewQuestion,
    DeleteQuestion,
)
from quiz.views.update_teacher import UpdateTeacher

urlpatterns = [
    path("debug/", include(debug_toolbar.urls)),
    path("admin/", admin.site.urls),
    path("teacher/", include("teacher.urls")),
    path("student/", include("student.urls")),
    path("", HomeView.as_view(), name="Home"),
    path("logout", LogoutView.as_view(template_name="quiz/logout.html"), name="logout"),
    path("aboutus", AboutUsView.as_view()),
    path("afterlogin", AfterLogin.as_view(name="afterlogin")),
    path("adminclick", AdminClick.as_view()),
    path(
        "adminlogin",
        LoginView.as_view(template_name="quiz/adminlogin.html"),
        name="adminlogin",
    ),
    path("admin-dashboard", AdminDashboard.as_view(), name="admin-dashboard"),
    path("admin-teacher", AdminTeacher.as_view(), name="admin-teacher"),
    path("admin-view-teacher", AdminView.as_view(), name="admin-view-teacher"),
    path("update-teacher/<int:pk>", UpdateTeacher.as_view(), name="update-teacher"),
    path("delete-teacher/<int:pk>", DeleteTeacher.as_view(), name="delete-teacher"),
    path(
        "admin-view-pending-teacher",
        AdminPendingTeacher.as_view(),
        name="admin-view-pending-teacher",
    ),
    path("approve-teacher/<int:pk>", ApproveTeacher.as_view(), name="approve-teacher"),
    path("reject-teacher/<int:pk>", RejectTeacher.as_view(), name="reject-teacher"),
    path("admin-student", AdminStudent.as_view(), name="admin-student"),
    path("admin-view-student", AdminStudentView.as_view(), name="admin-view-student"),
    path(
        "admin-view-student-marks",
        AdminStudentMarks.as_view(),
        name="admin-view-student-marks",
    ),
    path(
        "admin-view-marks/<int:pk>",
        AdminStudentMarksView.as_view(),
        name="admin-view-marks",
    ),
    path(
        "admin-check-marks/<int:pk>",
        AdminCheckMarks.as_view(),
        name="admin-check-marks",
    ),
    path("update-student/<int:pk>", UpdateStudent.as_view(), name="update-student"),
    path(
        "delete-student/<int:pk>", AdminDeleteStudent.as_view(), name="delete-student"
    ),
    path("admin-course", CourseView.as_view(), name="admin-course"),
    path("admin-add-course", AddCourse.as_view(), name="admin-add-course"),
    path("admin-view-course", CourseListView.as_view(), name="admin-view-course"),
    path("delete-course/<int:pk>", DeleteCourse.as_view(), name="delete-course"),
    path("admin-question", QuestionView.as_view(), name="admin-question"),
    path("admin-add-question", AddQuestion.as_view(), name="admin-add-question"),
    path("admin-view-question", QuestionListView.as_view(), name="admin-view-question"),
    path("view-question/<int:pk>", ViewQuestion.as_view(), name="view-question"),
    path("delete-question/<int:pk>", DeleteQuestion.as_view(), name="delete-question"),
]
