from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio (request):

    return render(request, "Star_wars_app/inicio.html")

def personajes (request):

    return render(request, "Star_wars_app/personajes.html")

def peliculas (request):

    return render(request, "Star_wars_app/peliculas.html")

def especies (request):

    return render(request, "Star_wars_app/especies.html")

def planetas (request):

    return render(request, "Star_wars_app/planetas.html")

def naves (request):

    return render(request, "Star_wars_app/naves.html")

def vehiculos (request):

    return render(request, "Star_wars_app/vehiculos.html")