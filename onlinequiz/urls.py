from django.contrib import admin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include

from quiz import views
from quiz.views.about_us import AboutUsView
from quiz.views.admin_click import AdminClick
from quiz.views.admin_dashboard import AdminDashboard
from quiz.views.admin_teacher import AdminTeacher, AdminView
from quiz.views.after_login import AfterLogin
from quiz.views.contact_us import ContactUsView
from quiz.views.home import HomeView
from quiz.views.update_teacher import UpdateTeacher

urlpatterns = [
    path("admin/", admin.site.urls),
    path("teacher/", include("teacher.urls")),
    path("student/", include("student.urls")),
    path("", HomeView.as_view(), name=""),
    path("logout", LogoutView.as_view(template_name="quiz/logout.html"), name="logout"),
    path("aboutus", AboutUsView.as_view()),
    path("contactus", ContactUsView.as_view()),
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
    # path("delete-teacher/<int:pk>", views.delete_teacher_view, name="delete-teacher"),
    # path(
    #     "admin-view-pending-teacher",
    #     views.admin_view_pending_teacher_view,
    #     name="admin-view-pending-teacher",
    # ),
    # path(
    #     "admin-view-teacher-salary",
    #     views.admin_view_teacher_salary_view,
    #     name="admin-view-teacher-salary",
    # ),
    # path(
    #     "approve-teacher/<int:pk>", views.approve_teacher_view, name="approve-teacher"
    # ),
    # path("reject-teacher/<int:pk>", views.reject_teacher_view, name="reject-teacher"),
    # path("admin-student", views.admin_student_view, name="admin-student"),
    # path(
    #     "admin-view-student", views.admin_view_student_view, name="admin-view-student"
    # ),
    # path(
    #     "admin-view-student-marks",
    #     views.admin_view_student_marks_view,
    #     name="admin-view-student-marks",
    # ),
    # path(
    #     "admin-view-marks/<int:pk>",
    #     views.admin_view_marks_view,
    #     name="admin-view-marks",
    # ),
    # path(
    #     "admin-check-marks/<int:pk>",
    #     views.admin_check_marks_view,
    #     name="admin-check-marks",
    # ),
    # path("update-student/<int:pk>", views.update_student_view, name="update-student"),
    # path("delete-student/<int:pk>", views.delete_student_view, name="delete-student"),
    # path("admin-course", views.admin_course_view, name="admin-course"),
    # path("admin-add-course", views.admin_add_course_view, name="admin-add-course"),
    # path("admin-view-course", views.admin_view_course_view, name="admin-view-course"),
    # path("delete-course/<int:pk>", views.delete_course_view, name="delete-course"),
    # path("admin-question", views.admin_question_view, name="admin-question"),
    # path(
    #     "admin-add-question", views.admin_add_question_view, name="admin-add-question"
    # ),
    # path(
    #     "admin-view-question",
    #     views.admin_view_question_view,
    #     name="admin-view-question",
    # ),
    # path("view-question/<int:pk>", views.view_question_view, name="view-question"),
    # path(
    #     "delete-question/<int:pk>", views.delete_question_view, name="delete-question"
    # ),
]
