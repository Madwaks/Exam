import pytest
from django.contrib.auth.models import User


@pytest.fixture(scope="session")
def mock_username() -> str:
    return "John"


@pytest.mark.django_db
@pytest.fixture(scope="session")
def mock_user(mock_username: str, db) -> User:
    return User.objects.create_user(
        mock_username, "lennon@thebeatles.com", "johnpassword"
    )
