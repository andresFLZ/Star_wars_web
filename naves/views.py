from django.shortcuts import render
from django.views.generic import ListView
from.models import Nave

def navesDetail (request):

    return render(request, "naves/naves_detail.html")

class NavesList(ListView):
    model = Nave
    template_name = "naves/naves_list.html"