from django.shortcuts import render
from django.views.generic import Listview
from .models import Personaje

def personajes (request):

    campos = ["nombre", "año nacimiento", "genero", "planeta origen", "peliculas", "especie", "naves espaciales", "vehiculos"]
    filas = [1, 2]

    return render(request, "personajes/personajes.html", {"campos" : campos, "filas" : filas, "bloques_s" : (len(campos) - ((len(campos)//3)*3))})

class PersonajesList(Listview):
    model = Personaje
    template_name = "personajes/personajes.html"
