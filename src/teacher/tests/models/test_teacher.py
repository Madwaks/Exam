import pytest
from django.contrib.auth.models import User

from teacher.models import Teacher


@pytest.mark.django_db
def test_teacher(mock_teacher: Teacher, mock_password: str, mock_username: str):
    assert mock_teacher.user.username == mock_username
    assert mock_teacher.user.check_password(mock_password)
    assert mock_teacher.full_name == mock_username
    assert str(mock_teacher) == mock_username
    assert mock_teacher.get_instance == mock_teacher
