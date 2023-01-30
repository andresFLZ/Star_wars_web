from django.urls import path
from planetas.views import PlanetasList, planetasDetail

app_name = 'planetas'
urlpatterns = [
    path('', PlanetasList.as_view(), name='Planetas'),
    path('detail/', planetasDetail, name="Detail"),
]