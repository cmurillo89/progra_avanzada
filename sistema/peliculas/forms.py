from django import forms
from .models import Pelicula, categoria

class PeliculaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=categoria.objects.all())
    class Meta:
        model = Pelicula
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = categoria
        fields = '__all__'