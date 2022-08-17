from django.urls import path

from . import views

urlpatterns = [
    path("", views.CartItemsList.as_view()),
    path("items/<int:pk>", views.CartItemsView.as_view()),
]
