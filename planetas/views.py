from django.shortcuts import render

def planetas (request):

    return render(request, "planetas/planetas.html")
