import pytest
from django.test import Client, RequestFactory
from django.urls import reverse
from quiz.models import Course
from teacher.models import Teacher
from teacher.views.exam import TeacherAddExam


@pytest.mark.django_db
def test_add_exam(
    mock_teacher: Teacher, request_factory: RequestFactory, client: Client
):
    url = reverse("teacher-add-exam")
    request = request_factory.get(url)
    request.user = mock_teacher
    view = TeacherAddExam()
    view.request = request
    breakpoint()
