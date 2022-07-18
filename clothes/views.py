from core.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from clothes.models import Cloth
from clothes.serializers import ClothCreateSerializer, ClothSerializer

from .filters import ClothFilter


class ClothesList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Cloth.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_class = ClothFilter

    def get_serializer_class(self):
        method = self.request.method
        if method == 'GET':
            return ClothSerializer
        return ClothCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
