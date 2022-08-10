import pytest
from django.contrib.auth import get_user_model

from ..models import Cloth

User = get_user_model()


@pytest.fixture
def user_instance() -> User:
    return User.objects.create(
        email="a@a.com", first_name="A", last_name="B", password="password"
    )


@pytest.fixture
def make_cloth():
    def _make_cloth(
        name,
        description,
        retail_price,
        sell_price,
        size,
        gender,
        color,
        category,
        owner,
    ) -> Cloth:
        return Cloth.objects.create(
            name=name,
            description=description,
            retail_price=retail_price,
            sell_price=sell_price,
            size=size,
            gender=gender,
            color=color,
            category=category,
            owner=owner,
        )

    return _make_cloth


@pytest.fixture
def cloth_instance(user_instance: User, make_cloth) -> Cloth:
    return make_cloth(
        name="Shirt",
        description="Red shirt with checkmarks",
        retail_price=1000,
        sell_price=500,
        size="M",
        gender="M",
        color="White",
        category="Shirt",
        owner=user_instance,
    )
