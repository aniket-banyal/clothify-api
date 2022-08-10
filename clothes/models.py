from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    MEN = "M"
    WOMEN = "W"

    GENDER_CHOICES = [
        (MEN, "Men"),
        (WOMEN, "Women"),
    ]

    BLAZER = "Blazer"
    CARDIGAN = "Cardigan"
    CASUAL_TROUSER = "Casual Trouser"
    FORMAL_TROUSER = "Formal Trouser"
    HOODIE = "Hoodie"
    JACKET = "Jacket"
    JEANS = "Jeans"
    POLO_SHIRT = "Polo shirt"
    PULLOVER = "Pullover"
    SHIRT = "Shirt"
    SHORTS = "Shorts"
    SLEEVELESS_SHIRT = "Sleeveless shirt"
    SUIT = "Suit"
    TSHIRT = "Tshirt"
    WAISTCOAT = "Waistcoat"

    MEN_CATEGORY_CHOICES = [
        (BLAZER, BLAZER),
        (CARDIGAN, CARDIGAN),
        (CASUAL_TROUSER, CASUAL_TROUSER),
        (FORMAL_TROUSER, FORMAL_TROUSER),
        (HOODIE, HOODIE),
        (JACKET, JACKET),
        (JEANS, JEANS),
        (POLO_SHIRT, POLO_SHIRT),
        (PULLOVER, PULLOVER),
        (SHIRT, SHIRT),
        (SHORTS, SHORTS),
        (SLEEVELESS_SHIRT, SLEEVELESS_SHIRT),
        (SUIT, SUIT),
        (TSHIRT, TSHIRT),
        (WAISTCOAT, WAISTCOAT),
    ]

    COAT = "Coat"
    DRESS = "Dress"
    HOODIE = "Hoodie"
    JACKET = "Jacket"
    JEANS = "Jeans"
    KURTA = "Kurta"
    SAREE = "Saree"
    SHEATH_DRESS = "Sheath dress"
    SHORTS = "Shorts"
    SHRUG = "Shrug"
    SKIRT = "Skirt"
    SUIT = "Suit"
    SWEATER = "Sweater"
    TOPS = "Tops"
    TSHIRT = "Tshirt"

    WOMEN_CATEGORY_CHOICES = [
        (COAT, COAT),
        (DRESS, DRESS),
        (HOODIE, HOODIE),
        (JACKET, JACKET),
        (JEANS, JEANS),
        (KURTA, KURTA),
        (SAREE, SAREE),
        (SHEATH_DRESS, SHEATH_DRESS),
        (SHORTS, SHORTS),
        (SHRUG, SHRUG),
        (SKIRT, SKIRT),
        (SUIT, SUIT),
        (SWEATER, SWEATER),
        (TOPS, TOPS),
        (TSHIRT, TSHIRT),
    ]

    NAME_CHOICES = list(dict.fromkeys(MEN_CATEGORY_CHOICES + WOMEN_CATEGORY_CHOICES))

    name = models.CharField(max_length=30, choices=NAME_CHOICES)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return f"{self.name} - {self.gender}"


class Cloth(models.Model):
    MIN_PRICE = 1

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

    name = models.CharField(max_length=200)
    description = models.TextField()
    retail_price = models.PositiveIntegerField(
        validators=[MinValueValidator(MIN_PRICE)]
    )
    sell_price = models.PositiveIntegerField(validators=[MinValueValidator(MIN_PRICE)])
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
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
