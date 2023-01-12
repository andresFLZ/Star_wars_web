from django.urls import path
from personajes import views

app_name = 'personajes'
urlpatterns = [
    path('', views.personajes, name='Personajes'),
]