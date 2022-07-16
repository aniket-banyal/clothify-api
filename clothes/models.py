from django.db import models


class Cloth(models.Model):
    EXTRA_EXTRA_SMALL = 'XXS'
    EXTRA_SMALL = 'XS'
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    EXTRA_LARGE = 'XL'
    EXTRA_EXTRA_LARGE = 'XXL'

    SIZE_CHOICES = [
        (EXTRA_EXTRA_SMALL, EXTRA_EXTRA_SMALL),
        (EXTRA_SMALL, EXTRA_SMALL),
        (SMALL, SMALL),
        (MEDIUM, MEDIUM),
        (LARGE, LARGE),
        (EXTRA_LARGE, EXTRA_LARGE),
        (EXTRA_EXTRA_LARGE, EXTRA_EXTRA_LARGE),
    ]

    MEN = 'M'
    WOMEN = 'W'
    OTHERS = 'O'

    GENDER_CHOICES = [
        (MEN, 'Men'),
        (WOMEN, 'Women'),
        (OTHERS, 'Others'),
    ]

    BEIGE = 'Beige'
    BLACK = 'Black'
    BLUE = 'Blue'
    BROWN = 'Brown'
    GREEN = 'Green'
    GREY = 'Grey'
    INDIGO = 'Indigo'
    MAROON = 'Maroon'
    MULTI = 'Multi'
    NAVY = 'Navy'
    NUDE = 'Nude'
    ORANGE = 'Orange'
    PINK = 'Pink'
    PURPLE = 'Purple'
    RED = 'Red'
    WHITE = 'White'
    YELLOW = 'Yellow'

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
    retail_price = models.PositiveIntegerField()
    sell_price = models.PositiveIntegerField()
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)

    class Meta:
        verbose_name_plural = "clothes"

    def __str__(self) -> str:
        return self.name
