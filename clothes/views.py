from core.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser

from clothes.models import Cloth
from clothes.serializers import ClothCreateSerializer, ClothSerializer

from .filters import ClothFilter
from .utils import uploadImage


class ClothesList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Cloth.objects.all()

    parser_classes = [MultiPartParser, FormParser]

    filter_backends = [DjangoFilterBackend]
    filterset_class = ClothFilter

    def get_serializer_class(self):
        method = self.request.method
        if method == 'GET':
            return ClothSerializer
        return ClothCreateSerializer

    def perform_create(self, serializer):
        image = self.request.data['cover_img']
        name: str = image.name + '_'.join([str(value) for value in serializer.validated_data.values()])
        cover_img_url = uploadImage(image=image, name=name)

        serializer.save(owner=self.request.user, cover_img_url=cover_img_url)
