from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm
# Create your views here.

def index(request): 
    items_table = ['id', 'Nombre', 'talla', 'observaciones' , 'marca', 'inventario', 'Imagen', 'Fecha', 'funciones']
    productos = Producto.objects.all()
    return render(request, 'catalogos\index.html', {'productos': productos, 'items': items_table})

def create(request):
    form_producto = ProductoForm
    return render(request, 'catalogos\create.html', {'form_producto': form_producto})

def edit(request):
    return render(request, 'catalogos\edit.html')

def store(request):
    print('datos')
    return  request