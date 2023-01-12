from django.urls import path
from planetas import views

app_name = 'planetas'
urlpatterns = [
    path('', views.planetas, name="Planetas"),
]