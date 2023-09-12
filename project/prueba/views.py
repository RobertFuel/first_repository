from django.shortcuts import render


def index(request):
    contexto = {"nombre": "Mi Primera App"}
    return render(request, "prueba/index.html", contexto)
