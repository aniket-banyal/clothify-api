from clothes.models import Cloth
from django.contrib.auth import get_user_model
from django.db import models


class Cart(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def get_items(self):
        return self.cartitem_set.all()

    def get_total(self):
        return sum(item.cloth.sell_price for item in self.get_items())

    def __str__(self) -> str:
        return f"Cart {self.user}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.cart} {self.cloth}"
