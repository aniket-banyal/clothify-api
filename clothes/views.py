from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from clothes.models import Category, Cloth
from clothes.serializers import (CategoryDetailSerializer,
                                 ClothCreateSerializer, ClothSerializer)

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

    def perform_create(self, serializer):
        image = self.request.data["cover_img"]
        name: str = image.name + "_".join(
            [str(value) for value in serializer.validated_data.values()]
        )
        cover_img_url = uploadImage(image=image, name=name)

        serializer.save(owner=self.request.user, cover_img_url=cover_img_url)


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
