from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Category(models.Model):
    MEN = "M"
    WOMEN = "W"

    GENDER_CHOICES = [
        (MEN, "Men"),
        (WOMEN, "Women"),
    ]

    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)

    class Meta:
        verbose_name_plural = "categories"

    def get_clothes_count(self) -> int:
        return self.cloth_set.all().count()

    def __str__(self):
        return f"{self.name} - {self.gender}"


class Cloth(models.Model):
    MIN_PRICE = 1
    MAX_PRICE = 10000

    EXTRA_EXTRA_SMALL = "XXS"
    EXTRA_SMALL = "XS"
    SMALL = "S"
    MEDIUM = "M"
    LARGE = "L"
    EXTRA_LARGE = "XL"
    EXTRA_EXTRA_LARGE = "XXL"

    SIZE_CHOICES = [
        (EXTRA_EXTRA_SMALL, EXTRA_EXTRA_SMALL),
        (EXTRA_SMALL, EXTRA_SMALL),
        (SMALL, SMALL),
        (MEDIUM, MEDIUM),
        (LARGE, LARGE),
        (EXTRA_LARGE, EXTRA_LARGE),
        (EXTRA_EXTRA_LARGE, EXTRA_EXTRA_LARGE),
    ]

    BEIGE = "Beige"
    BLACK = "Black"
    BLUE = "Blue"
    BROWN = "Brown"
    GREEN = "Green"
    GREY = "Grey"
    INDIGO = "Indigo"
    MAROON = "Maroon"
    MULTI = "Multi"
    NAVY = "Navy"
    NUDE = "Nude"
    ORANGE = "Orange"
    PINK = "Pink"
    PURPLE = "Purple"
    RED = "Red"
    WHITE = "White"
    YELLOW = "Yellow"

    COLOR_CHOICES = [
        (BEIGE, BEIGE),
        (BLACK, BLACK),
        (BLUE, BLUE),
        (BROWN, BROWN),
        (GREEN, GREEN),
        (GREY, GREY),
        (INDIGO, INDIGO),
        (MAROON, MAROON),
        (MULTI, MULTI),
        (NAVY, NAVY),
        (NUDE, NUDE),
        (ORANGE, ORANGE),
        (PINK, PINK),
        (PURPLE, PURPLE),
        (RED, RED),
        (WHITE, WHITE),
        (YELLOW, YELLOW),
    ]

    CHIFFON = "Chiffon"
    COTTON = "Cotton"
    CREPE = "Crepe"
    DENIM = "Denim"
    LACE = "Lace"
    LEATHER = "Leather"
    LINEN = "Linen"
    SATIN = "Satin"

    MATERIAL_CHOICES = [
        (CHIFFON, CHIFFON),
        (COTTON, COTTON),
        (CREPE, CREPE),
        (DENIM, DENIM),
        (LACE, LACE),
        (LEATHER, LEATHER),
        (LINEN, LINEN),
        (SATIN, SATIN),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    retail_price = models.PositiveIntegerField(
        validators=[MinValueValidator(MIN_PRICE), MaxValueValidator(MAX_PRICE)]
    )
    sell_price = models.PositiveIntegerField(
        validators=[MinValueValidator(MIN_PRICE), MaxValueValidator(MAX_PRICE)]
    )
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
    material = models.CharField(max_length=30, choices=MATERIAL_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cover_img_url = models.URLField()

    class Meta:
        verbose_name_plural = "clothes"

    def __str__(self) -> str:
        return self.name


class Image(models.Model):
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return self.url
