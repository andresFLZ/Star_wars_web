from django.shortcuts import render

def especies (request):

    return render(request, "especies/especies.html")
