from django.contrib import admin

from .models import Category, Cloth, Image

admin.site.register(Cloth)
admin.site.register(Image)
admin.site.register(Category)
