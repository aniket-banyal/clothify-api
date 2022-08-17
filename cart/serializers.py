from clothes.serializers import ClothSerializer
from rest_framework import serializers

from .models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    cloth = ClothSerializer()

    class Meta:
        model = CartItem
        fields = (
            "id",
            "cloth",
        )


class CartItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = (
            "cart",
            "cloth",
        )
        read_only_fields = ("cart",)
