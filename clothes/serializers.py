from rest_framework import serializers

from .models import Category, Cloth, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('url',)


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(source='get_name_display')
    gender = serializers.CharField(source='get_gender_display')

    class Meta:
        model = Category
        fields = ('name', 'gender')


class CategoryDetailSerializer(serializers.Serializer):
    name = serializers.CharField(source='get_name_display')
    gender = serializers.CharField(source='get_gender_display')

    class Meta:
        model = Category
        fields = ('name', 'gender')  # add image also


class ClothSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Cloth
        fields = ('id', 'name', 'retail_price', 'sell_price', 'cover_img_url', 'category')


class ClothDetailSerializer(serializers.ModelSerializer):

    size = serializers.CharField(source='get_size_display')
    color = serializers.CharField(source='get_color_display')
    category = CategorySerializer()
    images = serializers.SerializerMethodField()

    class Meta:
        model = Cloth
        fields = ('name', 'description', 'retail_price', 'sell_price', 'size', 'color', 'category', 'owner')

    def get_images(self, cloth: Cloth):
        images = [image.url for image in cloth.image_set.all()]
        return images


class ClothCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cloth
        fields = ('name', 'description', 'retail_price', 'sell_price', 'size', 'color', 'category', 'cover_img_url')
        read_only_fields = ('cover_img_url',)
