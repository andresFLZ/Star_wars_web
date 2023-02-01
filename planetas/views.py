from django.shortcuts import render
from django.views.generic import ListView, DetailView
from.models import Planeta
from peliculas.models import Pelicula

class PlanetasList(ListView):
    model = Planeta
    template_name = "planetas/planetas_list.html"

class PlanetasDetail(DetailView):
    model = Planeta
    template_name = "planetas/planetas_detail.html"

    def get_context_data(self, **kwargs):
        context = super(PlanetasDetail, self).get_context_data(**kwargs)
        context['peliculas'] = Pelicula.objects.all()
        
        return context