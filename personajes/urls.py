from django.urls import path
from personajes.views import PersonajesList, personajesDetail

app_name = 'personajes'
urlpatterns = [
    path('', PersonajesList.as_view(), name='Personajes'),
    path('detail/', personajesDetail, name='Detail'),
]