from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Vehiculo
from peliculas.models import Pelicula
from personajes.models import Personaje

class VehiculosList(ListView):
    model = Vehiculo
    template_name = "vehiculos/vehiculos_list.html"

class VehiculosDetail(DetailView):
    model = Vehiculo
    template_name = "vehiculos/vehiculos_detail.html"

    def get_context_data(self, **kwargs):
        context = super(VehiculosDetail, self).get_context_data(**kwargs)
        context['peliculas'] = Pelicula.objects.all()
        context['personajes'] = Personaje.objects.all()
        context['per'] = Personaje.objects.get(nombre='Luke Skywalker')
        
        return context