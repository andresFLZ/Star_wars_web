from django.urls import path
from vehiculos.views import VehiculosList, vehiculosDetail 

app_name = 'vehiculos'
urlpatterns = [
    path('', VehiculosList.as_view(), name='Vehiculos'),
    path('detail/', vehiculosDetail, name="Detail"),
]