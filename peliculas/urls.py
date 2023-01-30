from django.urls import path
from peliculas.views import PeliculasList, peliculasDetail

app_name = 'peliculas'
urlpatterns = [
    path('', PeliculasList.as_view(), name='Peliculas'),
    path('detail/', peliculasDetail, name='Detail'),
]