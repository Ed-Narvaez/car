# This Python file uses the following encoding: utf-8
from django.forms import ModelForm
from django import forms
from .models import Auto, Comentario, Marca, Tipo


class ContactoForm(forms.Form):
    correo = forms.EmailField(label='Tú correo electrónico')
    mensaje = forms.CharField(widget=forms.Textarea)

class AutoForm(ModelForm):
    class Meta:
        model = Auto
        fields = '__all__'
class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'
class TipoForm(ModelForm):
    class Meta:
        model = Tipo
        fields = '__all__'


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
