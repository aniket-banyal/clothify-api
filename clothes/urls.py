from django.urls import path

from . import views

urlpatterns = [
    path("", views.ClothesList.as_view()),
    path("<int:pk>", views.ClothesView.as_view()),
    path("categories", views.CategoryList.as_view()),
    path("colors", views.ColorList.as_view()),
    path("sizes", views.SizeList.as_view()),
    path("price-range", views.SellPriceRangeView.as_view()),
    path("cart", views.CartItemsList.as_view()),
]
