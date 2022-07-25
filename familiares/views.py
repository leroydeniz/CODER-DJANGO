from venv import create
from django.shortcuts import render
from familiares.models import Familiares

# Create your views here.
def nuevo_familiar(request):
    """
    Vista constructura de los objetos Familiares
    """

    # Crear el objeto en BD
    #nuevo_familiar = Familiares.objects.create(nombre="Juan Carlos", parentezco="Abuelo", tel = 123456, peso=80.5)
    nuevo_familiar = Familiares.objects.create(nombre="Manuel", parentezco="Hermano", tel = 345678, peso=55.8)
    
    # Definir el contexto a renderizar
    contexto = {
        "nuevo_familiar" : nuevo_familiar
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


def borrar_familiares(request):
    """
    Vista para limpiar la base de datos de familiares
    """

    # ELiminar los datos
    Familiares.objects.all().delete()

    # Renderizar el resultado
    return render(request, 'borrar_familiares.html', context={})