from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Especie
from peliculas.models import Pelicula

class EspeciesList(ListView):
    model = Especie
    template_name = "especies/especies_list.html"

class EspeciesDetail(DetailView):
    model = Especie
    template_name = "especies/especies_detail.html"

    def get_context_data(self, **kwargs):
        context = super(EspeciesDetail, self).get_context_data(**kwargs)
        context['peliculas'] = Pelicula.objects.all()
        
        return context