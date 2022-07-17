from django.urls import include, path

urlpatterns = [
    path('clothes/', include('clothes.urls')),
    path('users/', include('users.urls')),
]
