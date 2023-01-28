from django.urls import path
from personajes.views import PersonajesList, personajes, personajesDetail

app_name = 'personajes'
urlpatterns = [
    #path('', personajes, name='Personajes'),
    path('detail/', personajesDetail, name='Detail'),
    path('', PersonajesList.as_view(), name='Personajes'),
]