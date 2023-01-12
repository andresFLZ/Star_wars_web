from django.urls import path
from naves import views

app_name = 'naves'
urlpatterns = [
    path('', views.naves, name="Naves"),
]