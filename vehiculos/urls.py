from django.urls import path
from vehiculos.views import VehiculosList, VehiculosDetail 

app_name = 'vehiculos'
urlpatterns = [
    path('', VehiculosList.as_view(), name='Vehiculos'),
    path('detail/<int:pk>/', VehiculosDetail.as_view(), name="Detail"),
]