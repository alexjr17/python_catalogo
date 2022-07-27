from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'catalogos\index.html')

def create(request):
    return render(request, 'catalogos\create.html')

def edit(request):
    return render(request, 'catalogos\edit.html')