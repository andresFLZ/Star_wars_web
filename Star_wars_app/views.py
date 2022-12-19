from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio (request):

    return HttpResponse("Inicio")

def personajes (request):

    return HttpResponse("Personajes")

def peliculas (request):

    return HttpResponse("Peliculas")

def especies (request):

    return HttpResponse("Especies")

def planetas (request):

    return HttpResponse("Planetas")

def naves (request):

    return HttpResponse("Naves")

def vehiculos (request):

    return HttpResponse("Vehiculos")