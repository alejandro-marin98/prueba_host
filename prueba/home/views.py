from django.shortcuts import render
from django.http import HttpResponse
from solicitudes import views as sol


def home(request):
    solic = list(sol.getSolicitudes())
    return render(request, 'home.html', {'cantidadSolicitudes': len(solic)})
