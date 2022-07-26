from rest_framework import serializers

from .models import Cloth, Image


class ClothSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source='get_gender_display')

    class Meta:
        model = Cloth
        fields = ('id', 'name', 'retail_price', 'sell_price', 'gender', 'cover_img_url')


class ClothDetailSerializer(serializers.ModelSerializer):

    size = serializers.CharField(source='get_size_display')
    gender = serializers.CharField(source='get_gender_display')
    color = serializers.CharField(source='get_color_display')
    category = serializers.CharField(source='get_category_display')
    images = serializers.SerializerMethodField()

    class Meta:
        model = Cloth
        fields = ('name', 'description', 'retail_price', 'sell_price', 'size', 'gender', 'color', 'category', 'owner')

    def get_images(self, cloth: Cloth):
        images = [image.url for image in cloth.image_set.all()]
        return images


class ClothCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloth
        fields = ('name', 'description', 'retail_price', 'sell_price', 'size', 'gender', 'color', 'category', 'cover_img_url')
        read_only_fields = ('cover_img_url',)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('url',)
