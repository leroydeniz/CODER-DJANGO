"""MVT_LeroyDeniz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from familiares.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nuevo_familiar/', nuevo_familiar, name='nuevo_familiar'),
    path('listar_familiares/', listar_familiares, name='listar_familiares'),
    path('borrar_familiares/', borrar_familiares, name='borrar_familiares'),
]
