from django.forms import ModelForm
from proyecto.models import *

class AgresorForm(ModelForm):
    class Meta:
         model = Agresor
         fields = ['nombres', 'apellidos', 'edad', 'nacionalidad', 'ocupacion']

class VictimaForm(ModelForm):
    class Meta:
         model = Victima
         fields = ['nombres', 'apellidos', 'edad', 'nacionalidad', 'ocupacion','causa']

class FemicidioForm(ModelForm):
    class Meta:
         model = Femicidio
         fields = ['fecha', 'hora', 'circunstancia', 'tipo_arma', 'testigo','agresor','victima']
