from django.shortcuts import render
from django.views.generic import ListView, DetailView
from.models import Pelicula

class PeliculasList(ListView):
    model = Pelicula
    template_name = "peliculas/peliculas_list.html"

class PeliculasDetail(DetailView):
    model = Pelicula
    template_name = "peliculas/peliculas_detail.html"
