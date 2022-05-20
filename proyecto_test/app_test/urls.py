from django.urls import path
from . import views



urlpatterns = [
    path("", views.inicio),
    path("curso" , views.curso),
    path("nuevo_curso/<nombre>" , views.alta_curso),
    path("alta_alumno/<nombre>",views.alta_alumno)
]