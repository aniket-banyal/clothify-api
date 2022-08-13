import os
import random
import string

from django.apps import apps
from django.conf import settings

project_name = "core"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{project_name}.settings")
apps.ready = False
apps.populate(settings.INSTALLED_APPS)


def create_clothes(n, color=None):
    from clothes.models import Category, Cloth
    from users.models import User

    user = User.objects.get(email="aman@gmail.com", password="aman")

    names = [
        x[0] for x in Category.MEN_CATEGORY_CHOICES + Category.WOMEN_CATEGORY_CHOICES
    ]
    categories = list(Category.objects.all())
    cover_img_urls = [
        "https://res.cloudinary.com/dummy26/image/upload/v1659251819/tshirt.jpgTshirt_Navy%20blue%20tshirt_900_300_M_Black_Blazer%20-%20M.jpg",
        "https://res.cloudinary.com/dummy26/image/upload/v1658680486/quickstart_butterfly.jpg",
        "https://res.cloudinary.com/dummy26/image/upload/v1658566382/cld-sample-5.jpg",
        "https://res.cloudinary.com/dummy26/image/upload/v1658566355/sample.jpg",
        "https://res.cloudinary.com/dummy26/image/upload/v1658566382/cld-sample-4.jpg",
        "https://res.cloudinary.com/dummy26/image/upload/v1658566381/cld-sample-2.jpg",
    ]

    for _ in range(n):
        Cloth.objects.create(
            name=random.sample(names, 1)[0],
            description=" ".join(
                [
                    "".join(
                        random.choices(string.ascii_letters, k=random.randrange(2, 10))
                    )
                    for _ in range(random.randrange(30, 100))
                ]
            ),
            retail_price=random.randint(1000, 2000),
            sell_price=random.randint(200, 800),
            size=random.sample([x[0] for x in Cloth.SIZE_CHOICES], 1)[0],
            color=color
            if color is not None
            else random.sample([x[0] for x in Cloth.COLOR_CHOICES], 1)[0],
            category=random.sample(categories, 1)[0],
            owner=user,
            cover_img_url=random.sample(cover_img_urls, 1)[0],
        )

    print("Done")


n = 60
# color = 'Blue'
# create_clothes(n, color=color)
create_clothes(n)
