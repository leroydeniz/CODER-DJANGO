from venv import create
from django.shortcuts import render
from familiares.models import Familiares

# Create your views here.
def crear_familiar(request):
    """
    Vista constructura de los objetos Familiares
    """

    # Crear el objeto en BD
    nuevo_familiar = Familiares.objects,create(nombre="Nombre del familiar 1", tel = 456985267, peso=65.6)
    
    # Definir el contexto a renderizar
    contexto = {
        "nuevo_familar" : nuevo_familiar
    }

    # Renderizar el resultado
    return render(request, 'nuevo_familiar.html', contexto)


def listar_familiares(request):
    """
    Vista para mostrar la lista de familiares
    """

    # Pedir a la BD todos los familiares guardados
    familiares = Familiares.objects.all()
    
    # Definir el contexto a renderizar
    contexto = {
        "familiares" : familiares
    }

    # Renderizar el resultado
    return render(request, 'listar_familiares.html', contexto)
