from rest_framework import serializers

from .models import Category, Cloth, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("url", "cloth")


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="get_name_display")

    class Meta:
        model = Category
        fields = ("id", "name", "gender")


class CategoryDetailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="get_name_display")

    class Meta:
        model = Category
        fields = ("id", "name", "gender")  # add image also


class ClothSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Cloth
        fields = (
            "id",
            "name",
            "retail_price",
            "sell_price",
            "cover_img_url",
            "category",
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
            "category",
            "cover_img_url",
        )
        read_only_fields = (
            "id",
            "cover_img_url",
        )
