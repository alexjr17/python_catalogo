from django.shortcuts import render
from .models import Producto
# Create your views here.

def index(request): 
    productos = Producto.objects.all()
    print(productos)
    return render(request, 'catalogos\index.html', {'productos': productos})

def create(request):
    return render(request, 'catalogos\create.html')

def edit(request):
    return render(request, 'catalogos\edit.html')