from django.urls import path
from especies.views import EspeciesList, especiesDetail

app_name = 'especies'
urlpatterns = [
    path('', EspeciesList.as_view(), name='Especies'),
    path('detail/', especiesDetail, name="Detail"),
]