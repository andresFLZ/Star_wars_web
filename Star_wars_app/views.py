from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio (request):

    return render(request, "Star_wars_app/inicio.html")
