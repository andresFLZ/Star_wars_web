from django.shortcuts import render
from django.views.generic import ListView
from.models import Planeta

def planetasDetail (request):

    return render(request, "planetas/planetas_detail.html")

class PlanetasList(ListView):
    model = Planeta
    template_name = "planetas/planetas_list.html"