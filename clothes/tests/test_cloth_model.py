import pytest
from clothes.models import Cloth


@pytest.mark.django_db
class TestClothModel:
    @pytest.mark.parametrize(
        "name, description, retail_price, sell_price, size, gender, color, category",
        [
            (
                "Shirt",
                "Red shirt with checkmarks",
                1000,
                500,
                "M",
                "M",
                "White",
                "Shirt",
            ),
            (
                "Kurta",
                "Casual Kurta in excellent condition",
                800,
                200,
                "L",
                "W",
                "Yellow",
                "Kurta",
            ),
        ],
    )
    def test_cloth_model_insert_data(
        self,
        make_cloth,
        user_instance,
        name,
        description,
        retail_price,
        sell_price,
        size,
        gender,
        color,
        category,
    ):
        owner = user_instance
        cloth: Cloth = make_cloth(
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

        assert cloth.name == name
        assert cloth.description == description
        assert cloth.retail_price == retail_price
        assert cloth.sell_price == sell_price
        assert cloth.size == size
        assert cloth.gender == gender
        assert cloth.color == color
        assert cloth.category == category
        assert cloth.owner == owner
