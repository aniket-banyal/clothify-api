from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import AllowAny

from clothes.models import Cloth
from clothes.serializers import ClothSerializer

from .filters import ClothFilter


class ClothesList(generics.ListAPIView):
    permission_classes = [AllowAny]

    queryset = Cloth.objects.all()
    serializer_class = ClothSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = ClothFilter
