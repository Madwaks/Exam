import pytest
from django.contrib.auth.models import User

from teacher.models import Teacher


@pytest.mark.django_db
def test_create_teacher(mock_user: User):
    teacher = Teacher()
    teacher.user = mock_user
    assert teacher.user.username == "John"
