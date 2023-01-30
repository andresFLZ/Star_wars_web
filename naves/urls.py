from django.urls import path
from naves.views import NavesList, navesDetail 

app_name = 'naves'
urlpatterns = [
    path('', NavesList.as_view(), name='Naves'),
    path('detail/', navesDetail, name="Detail"),
]