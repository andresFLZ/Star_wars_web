from django.shortcuts import render

def naves (request):

    return render(request, "naves/naves.html")
