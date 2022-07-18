from rest_framework import serializers
from .models import Cloth


class ClothSerializer(serializers.ModelSerializer):

    size = serializers.CharField(source='get_size_display')
    gender = serializers.CharField(source='get_gender_display')
    color = serializers.CharField(source='get_color_display')
    category = serializers.CharField(source='get_category_display')

    class Meta:
        model = Cloth
        fields = ('name', 'description', 'retail_price', 'sell_price', 'size', 'gender', 'color', 'category', 'owner')


class ClothCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloth
        fields = ('name', 'description', 'retail_price', 'sell_price', 'size', 'gender', 'color', 'category')
