from django.urls import path

from . import views

urlpatterns = [
    path('', views.ClothesList.as_view()),
    path('categories', views.CategoryList.as_view()),
    path('colors', views.ColorList.as_view()),
]
