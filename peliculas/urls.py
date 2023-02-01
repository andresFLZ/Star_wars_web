from django.urls import path
from peliculas.views import PeliculasList, PeliculasDetail

app_name = 'peliculas'
urlpatterns = [
    path('', PeliculasList.as_view(), name='Peliculas'),
    path('detail/<int:pk>/', PeliculasDetail.as_view(), name='Detail'),
]