from django.urls import path
from planetas.views import PlanetasList, PlanetasDetail

app_name = 'planetas'
urlpatterns = [
    path('', PlanetasList.as_view(), name='Planetas'),
    path('detail/<int:pk>/', PlanetasDetail.as_view(), name="Detail"),
]