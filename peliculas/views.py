from django.shortcuts import render
from django.views.generic import ListView
from.models import Pelicula

def peliculasDetail (request):

    return render(request, "peliculas/peliculas_detail.html")

class PeliculasList(ListView):
    model = Pelicula
    template_name = "peliculas/peliculas_list.html"