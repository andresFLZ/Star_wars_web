from django.shortcuts import render
from django.views.generic import ListView
from .models import Vehiculo

def vehiculosDetail (request):

    return render(request, "vehiculos/vehiculos_detail.html")

class VehiculosList(ListView):
    model = Vehiculo
    template_name = "vehiculos/vehiculos_list.html"
