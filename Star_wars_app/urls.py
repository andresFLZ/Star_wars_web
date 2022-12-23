from django.urls import path
from Star_wars_app import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('personajes/', views.personajes, name='Personajes'),
    path('peliculas/', views.peliculas, name='Peliculas'),
    path('especies/', views.especies, name="Especies"),
    path('planetas/', views.planetas, name="Planetas"),
    path('naves/', views.naves, name="Naves"),
    path('vehiculos/', views.vehiculos, name="Vehiculos"),
]