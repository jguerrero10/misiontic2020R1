from django.db.models import fields
from django.forms import ModelForm
from loanapp.models import *

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'