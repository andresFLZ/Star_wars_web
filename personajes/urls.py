from django.urls import path
from personajes.views import PersonajesList, PersonajesDetail

app_name = 'personajes'
urlpatterns = [
    path('', PersonajesList.as_view(), name='Personajes'),
    path('detail/<int:pk>/', PersonajesDetail.as_view(), name='Detail'),
]