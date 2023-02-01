from django.urls import path
from naves.views import NavesList, NavesDetail 

app_name = 'naves'
urlpatterns = [
    path('', NavesList.as_view(), name='Naves'),
    path('detail/<int:pk>/', NavesDetail.as_view(), name="Detail"),
]