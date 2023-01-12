from django.shortcuts import render

def vehiculos (request):

    return render(request, "vehiculos/vehiculos.html")
