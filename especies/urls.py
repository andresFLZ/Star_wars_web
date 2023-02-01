from django.urls import path
from especies.views import EspeciesList, EspeciesDetail

app_name = 'especies'
urlpatterns = [
    path('', EspeciesList.as_view(), name='Especies'),
    path('detail/<int:pk>/', EspeciesDetail.as_view(), name="Detail"),
]