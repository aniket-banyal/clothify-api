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

    GENDER_CHOICES = [
        (MEN, 'Men'),
        (WOMEN, 'Women'),
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

    BLAZER = 'Blazer'
    CARDIGAN = 'Cardigan'
    CASUAL_TROUSER = 'Casual Trouser'
    FORMAL_TROUSER = 'Formal Trouser'
    HOODIE = 'Hoodie'
    JACKET = 'Jacket'
    JEANS = 'Jeans'
    POLO_SHIRT = 'Polo shirt'
    PULLOVER = 'Pullover'
    SHIRT = 'Shirt'
    SHORTS = 'Shorts'
    SLEEVELESS_SHIRT = 'Sleeveless shirt'
    SUIT = 'Suit'
    TSHIRT = 'Tshirt'
    WAISTCOAT = 'Waistcoat'

    MEN_CATEGORY_CHOICES = set([
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
    ])

    COAT = 'Coat'
    DRESS = 'Dress'
    HOODIE = 'Hoodie'
    JACKET = 'Jacket'
    JEANS = 'Jeans'
    KURTA = 'Kurta'
    SAREE = 'Saree'
    SHEATH_DRESS = 'Sheath dress'
    SHORTS = 'Shorts'
    SHRUG = 'Shrug'
    SKIRT = 'Skirt'
    SUIT = 'Suit'
    SWEATER = 'Sweater'
    TOPS = 'Tops'
    TSHIRT = 'Tshirt'

    WOMEN_CATEGORY_CHOICES = set([
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
    ])

    CATEGORY_CHOICES = MEN_CATEGORY_CHOICES.union(WOMEN_CATEGORY_CHOICES)

    name = models.CharField(max_length=200)
    description = models.TextField()
    retail_price = models.PositiveIntegerField()
    sell_price = models.PositiveIntegerField()
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)

    class Meta:
        verbose_name_plural = "clothes"

    def __str__(self) -> str:
        return self.name
