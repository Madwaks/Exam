from django.contrib.auth.models import User
import pytest
from django.test import RequestFactory

from teacher.models import Teacher


@pytest.fixture(scope="session")
def request_factory() -> RequestFactory:
    return RequestFactory()


@pytest.fixture(scope="session")
def mock_username() -> str:
    return "John"


@pytest.fixture(scope="session")
def mock_password() -> str:
    return "lennon"


@pytest.fixture(scope="function")
def mock_user(mock_username: str, mock_password: str, db: None) -> User:
    return User.objects.create_user(username=mock_username, password=mock_password)


@pytest.mark.django_db
@pytest.fixture(scope="session")
def mock_teacher(mock_user: User) -> Teacher:
    return Teacher(user=mock_user)
