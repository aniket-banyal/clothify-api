from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.Clothes.as_view()),
]
