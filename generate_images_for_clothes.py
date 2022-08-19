import os
import random

from django.apps import apps
from django.conf import settings

project_name = "core"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{project_name}.settings")
apps.ready = False
apps.populate(settings.INSTALLED_APPS)


def create_images(n):
    from clothes.models import Cloth, Image

    img_urls = [
        "https://res.cloudinary.com/dummy26/image/upload/v1660387637/tshirtO_D_y_n_B_K_m_v_b_rjpg.jpg",
        "https://res.cloudinary.com/dummy26/image/upload/v1658680486/quickstart_butterfly.jpg",
        "https://res.cloudinary.com/dummy26/image/upload/v1658566382/cld-sample-5.jpg",
        "https://res.cloudinary.com/dummy26/image/upload/v1658566355/sample.jpg",
        "https://res.cloudinary.com/dummy26/image/upload/v1658566382/cld-sample-4.jpg",
        "https://res.cloudinary.com/dummy26/image/upload/v1658566381/cld-sample-2.jpg",
    ]

    for cloth in Cloth.objects.all():
        for _ in range(n):
            Image.objects.create(
                cloth=cloth,
                url=random.sample(img_urls, 1)[0],
            )

    print("Done")


n = 5
create_images(n)
