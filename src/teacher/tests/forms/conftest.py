import pytest

from teacher.forms.teacher import TeacherUserForm


@pytest.fixture(scope="module")
def mock_teacher_form() -> TeacherUserForm:
    return TeacherUserForm()
