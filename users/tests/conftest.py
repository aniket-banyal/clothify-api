import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def make_user():
    def _make_user(first_name, last_name, email, password) -> User:
        return User.objects.create(
            first_name=first_name, last_name=last_name, email=email, password=password
        )

    return _make_user
