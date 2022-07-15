from rest_framework import generics
from rest_framework.permissions import AllowAny
from clothes.models import Cloth

from clothes.serializers import ClothSerializer


class Clothes(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ClothSerializer
    queryset = Cloth.objects.all()
