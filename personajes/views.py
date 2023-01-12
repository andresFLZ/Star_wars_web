from django.shortcuts import render

def personajes (request):

    return render(request, "personajes/personajes.html")
