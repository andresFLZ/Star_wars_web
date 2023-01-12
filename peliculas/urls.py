from django.urls import path
from peliculas import views

app_name = 'peliculas'
urlpatterns = [
    path('', views.peliculas, name='Peliculas'),
]