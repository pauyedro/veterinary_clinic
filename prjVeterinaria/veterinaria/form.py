from .models import Localidad, Cliente, Tipo_Doc, Mascota, Provincia, Pais
from django.forms import ModelForm


class PaisForm(ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'


class ProvinciaForm(ModelForm):
    class Meta:
        model = Provincia
        fields = '__all__'


class LocalidadForm(ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'


class MascotaForm(ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'


class Tipo_DocForm(ModelForm):
    class Meta:
        model = Tipo_Doc
        fields = '__all__'


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'