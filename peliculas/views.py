from django.shortcuts import render

def peliculas (request):

    return render(request, "peliculas/peliculas.html")