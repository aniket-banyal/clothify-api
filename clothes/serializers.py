from rest_framework import serializers
from .models import Cloth


class ClothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloth
        fields = ('name', 'description', 'retail_price', 'sell_price')
