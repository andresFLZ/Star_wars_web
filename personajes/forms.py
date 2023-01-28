from django.forms import ModelForm
from .models import Personaje

class PersonajeForm(ModelForm):
    class Meta:
        model = Personaje
        fields = ["nombre"]