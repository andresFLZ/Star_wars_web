from django.urls import path
from vehiculos import views

app_name = 'vehiculos'
urlpatterns = [
    path('', views.vehiculos, name="Vehiculos"),
]