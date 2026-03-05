from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio),
    path("heroe/", views.crear_heroe),
    path("villano/", views.crear_villano),
    path("comic/", views.crear_comic),
    path("buscar/", views.buscar_heroe),
]