from django.shortcuts import render
from django.views.generic import ListView
from .models import Personaje

def personajesDetail (request):

    return render(request, "personajes/personajes_detail.html")


class PersonajesList(ListView):
    model = Personaje
    template_name = "personajes/personajes_list.html"
