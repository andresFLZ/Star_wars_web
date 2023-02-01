from django.shortcuts import render
from django.views.generic import ListView, DetailView
from.models import Nave
from peliculas.models import Pelicula
from personajes.models import Personaje

class NavesList(ListView):
    model = Nave
    template_name = "naves/naves_list.html"

class NavesDetail(DetailView):
    model = Nave
    template_name = "naves/naves_detail.html"

    def get_context_data(self, **kwargs):
        context = super(NavesDetail, self).get_context_data(**kwargs)
        context['peliculas'] = Pelicula.objects.all()
        context['personajes'] = Personaje.objects.all()
        context['per'] = Personaje.objects.get(nombre='Luke Skywalker')
        
        return context