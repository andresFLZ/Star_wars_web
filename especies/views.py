from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Especie

def especiesDetail (request):

    return render(request, "especies/especies_detail.html")

class EspeciesList(ListView):
    model = Especie
    template_name = "especies/especies_list.html"