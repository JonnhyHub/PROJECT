from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Inicio(request): 
    return render(request, 'paginas/Inicio.html')

def Nosotros(request): 
    return render(request, 'paginas/Nosotros.html')

def Usuarios(request):
    return render(request, 'Usuarios/index.html')

def crear_usuario(request):
    return render(request, 'Usuarios/crear.html')
    
def actualizar_usuario(request):
    return render(request, 'Usuarios/editar.html')

def Departamentos(request):
    return render(request, 'Departamentos/index.html')

def crear_departamento(request):
    return render(request, 'Departamentos/creardep.html')

def actualizar_departamento(request):
    return render(request, 'Departamentos/editardep.html')