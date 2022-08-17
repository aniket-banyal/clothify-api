import random
import string

from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from clothes.models import CartItem, Category, Cloth
from clothes.serializers import (
    CartItemCreateSerializer,
    CartItemSerializer,
    CategoryDetailSerializer,
    ClothCreateSerializer,
    ClothDetailSerializer,
    ClothSerializer,
    ImageSerializer,
)

from .filters import ClothFilter
from .utils import uploadImage


class CustomPagination(PageNumberPagination):
    page_size_query_param = "limit"


class ClothesList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Cloth.objects.all()

    parser_classes = [MultiPartParser, FormParser]

    filter_backends = [DjangoFilterBackend]
    filterset_class = ClothFilter

    pagination_class = CustomPagination

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return ClothSerializer
        return ClothCreateSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cloth = response.data.get("id")

        # https://stackoverflow.com/questions/27785292/django-rest-framework-uploading-multiple-files
        images = request.FILES.getlist("images")
        image_urls = []
        for image in images:
            img_name, img_ext = image.name.split(".")
            name: str = (
                img_name
                + "_".join(
                    [str(value) for value in random.sample(string.ascii_letters, 10)]
                )
                + img_ext
            )

            image_urls.append(
                {"url": uploadImage(image=image, name=name), "cloth": cloth}
            )

        img_serializer = ImageSerializer(data=image_urls, many=True)
        img_serializer.is_valid(raise_exception=True)
        img_serializer.save()

        return response

    def perform_create(self, serializer):
        image = self.request.data["cover_img"]
        img_name, img_ext = image.name.split(".")
        name: str = (
            img_name
            + "_".join([str(value) for value in serializer.validated_data.values()])
            + img_ext
        )
        cover_img_url = uploadImage(image=image, name=name)

        serializer.save(owner=self.request.user, cover_img_url=cover_img_url)


class ClothesView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Cloth.objects.all()

    lookup_field = "pk"

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return ClothDetailSerializer


class CategoryList(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Category.objects.all()

    serializer_class = CategoryDetailSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["gender"]


class ColorList(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        colors = [color_choices[0] for color_choices in Cloth.COLOR_CHOICES]
        return Response(data=colors)


class SizeList(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        sizes = [size_choices[0] for size_choices in Cloth.SIZE_CHOICES]
        return Response(data=sizes)


class SellPriceRangeView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        min_price = Cloth.MIN_PRICE
        max_price = Cloth.MAX_PRICE

        return Response(data={"min_price": min_price, "max_price": max_price})


class CartItemsList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return CartItemSerializer
        return CartItemCreateSerializer

    def create(self, request, *args, **kwargs):
        cart = request.user.cart
        cloth = get_object_or_404(Cloth, pk=request.data["cloth"])

        if CartItem.objects.filter(cart=cart, cloth=cloth).exists():
            return Response(
                data={"error": "Cloth is already present in your cart"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(cart=self.request.user.cart)
