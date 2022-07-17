from django.urls import path

from . import views

urlpatterns = [
    path('', views.ClothesList.as_view()),
]
