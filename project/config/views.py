from django.http import HttpResponse


def saludo(request):
    return HttpResponse("Hola Django 👋")


def saludo_con_input(request):
    nombre = input("Dime tu nombre: ")
    return HttpResponse(f"Hola {nombre.upper()}")


def numero_aleatorio(request):
    import random

    numero = random.randint(1, 6)
    if numero == 6:
        return HttpResponse(f"Has tirado el dado {numero} ✨tuviste suerte!!")
    else:
        return HttpResponse(f"Has tirado el dado {numero} Sigue intentando...")
