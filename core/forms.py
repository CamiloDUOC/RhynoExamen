from django import forms
from django.forms import ModelForm
from .models import Producto


class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields=['id','nombre', 'categoria', 'precio', 'descripcion']