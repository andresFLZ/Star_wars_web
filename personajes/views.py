from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Personaje
from peliculas.models import Pelicula
from especies.models import Especie

class PersonajesList(ListView):
    model = Personaje
    template_name = "personajes/personajes_list.html"

class PersonajesDetail(DetailView):
    model = Personaje
    template_name = "personajes/personajes_detail.html"

    def get_context_data(self, **kwargs):
        context = super(PersonajesDetail, self).get_context_data(**kwargs)
        context['peliculas'] = Pelicula.objects.all()
        context['especies'] = Especie.objects.all()
        context['esp'] = Especie.objects.get(nombre='Human')
        
        return context