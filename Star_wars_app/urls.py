from django.urls import path
from Star_wars_app import views

app_name = 'Star_wars_app'
urlpatterns = [
    path('', views.inicio, name='Inicio'),
]