from django.urls import path
from especies import views

app_name = 'especies'
urlpatterns = [
    path('', views.especies, name="Especies"),
]