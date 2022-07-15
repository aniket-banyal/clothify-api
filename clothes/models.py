from pyexpat import model
from django.db import models


class Cloth(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    retail_price = models.PositiveIntegerField()
    sell_price = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "clothes"
