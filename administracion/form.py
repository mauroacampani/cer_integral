from django import forms
from portal.models import Users, Profesional, Especialidad, Ocupacion

class ProfesionalForm(forms.ModelForm):
    class Meta:
        model = Profesional
        fields = '__all__'
        exclude = ('user',)

        
class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ['nombre']


class OcupacionForm(forms.ModelForm):
    class Meta:
        model = Ocupacion
        fields = '__all__'