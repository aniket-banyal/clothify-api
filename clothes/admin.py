from django.contrib import admin

from .models import Cart, Category, Cloth, Image

admin.site.register(Cloth)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Cart)
