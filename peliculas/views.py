from django.shortcuts import render
from django.views.generic import ListView, DetailView
from.models import Pelicula

class PeliculasList(ListView):
    model = Pelicula
    template_name = "peliculas/peliculas_list.html"

class PeliculasDetail(DetailView):
    model = Pelicula
    template_name = "peliculas/peliculas_detail.html"

    """def get_context_data(self, **kwargs):
        context = super(PersonajesDetail, self).get_context_data(**kwargs)
        context['peliculas'] = Pelicula.objects.all()
        context['especies'] = Especie.objects.all()
        context['esp'] = Especie.objects.get(nombre='Human')
        
        return context"""