import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.db.utils import IntegrityError

User = get_user_model()


@pytest.mark.django_db
class TestUserModel:
    @pytest.mark.parametrize(
        "first_name, last_name, email, password",
        [
            ("Aniket", "Banyal", "aniket@gmail.com", "aniket"),
            ("Aman", "Sharma", "aman@gmail.com", "aman"),
        ],
    )
    def test_user_model_insert_data(
        self, make_user, first_name, last_name, email, password
    ):
        user: User = make_user(
            first_name=first_name, last_name=last_name, email=email, password=password
        )

        assert user.first_name == first_name
        assert user.last_name == last_name
        assert user.email == email
        assert check_password(password, user.password) is True

    def test_duplicate_email(self, make_user):
        first_name = "Aniket"
        last_name = "Banyal"
        email = "aniket@gmail.com"
        password = "aniket"

        make_user(
            first_name=first_name, last_name=last_name, email=email, password=password
        )

        with pytest.raises(
            IntegrityError, match=r"UNIQUE constraint failed: [a-zA-Z_]+.email"
        ):
            make_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
            )
