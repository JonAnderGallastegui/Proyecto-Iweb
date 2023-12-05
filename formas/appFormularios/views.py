from django.shortcuts import render
from django.http import HttpResponse


def show_form(request):
    return render(request, 'registro.html')

def post_form(request):
    usuario = request.POST["usuario"]
    email = request.POST["email"]
    return HttpResponse(f"El usuario es {usuario} y el email {email}")

