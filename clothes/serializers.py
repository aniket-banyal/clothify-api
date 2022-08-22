from rest_framework import serializers

from .models import Category, Cloth, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("url", "cloth")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "gender")


class CategoryDetailSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(source="get_clothes_count")

    class Meta:
        model = Category
        fields = ("id", "name", "gender", "count")  # add image also


class ClothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloth
        fields = (
            "id",
            "name",
            "retail_price",
            "sell_price",
            "cover_img_url",
        )


class ClothDetailSerializer(serializers.ModelSerializer):
    size = serializers.CharField(source="get_size_display")
    color = serializers.CharField(source="get_color_display")
    images = serializers.SerializerMethodField("get_images")
    category_name = serializers.CharField(source="category.name")
    gender = serializers.CharField(source="category.gender")

    class Meta:
        model = Cloth
        fields = (
            "name",
            "description",
            "retail_price",
            "sell_price",
            "size",
            "color",
            "material",
            "category_name",
            "gender",
            "owner",
            "cover_img_url",
            "images",
        )

    def get_images(self, cloth: Cloth):
        images = [image.url for image in cloth.image_set.all()]
        return images


class ClothCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloth
        fields = (
            "id",
            "name",
            "description",
            "retail_price",
            "sell_price",
            "size",
            "color",
            "material",
            "category",
            "cover_img_url",
        )
        read_only_fields = (
            "id",
            "cover_img_url",
        )
