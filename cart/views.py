from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import CartItem, Cloth
from .serializers import CartItemCreateSerializer, CartItemSerializer


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


class CartItemsView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)
