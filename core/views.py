from urllib import request
from django.shortcuts import render, redirect
from core.forms import ProductoForm
from core.models import Producto, Categoria


# Create your views here.

def home(request):
    return render(request, 'core/home.html')


def builds (request):
    productos= Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'core/builds.html', datos)


def form_producto(request):
    datos = {
        'form': ProductoForm()
    }
    if request.method== 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"
    return render(request, 'core/form_producto.html',datos)

def form_mod_producto(request, id):
    producto = Producto.objects.get(id=id)
    datos = {
        'form': ProductoForm(instance=producto)
    }

    if request.method== 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Modificados Correctamente"
    return render(request, 'core/form_mod_producto.html', datos)

def form_del_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect(to="home")

def contacto(request):
    return render(request, 'core/contacto.html')


def login(request):
    return render(request, 'core/login.html')
