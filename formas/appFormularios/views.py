from django.shortcuts import render
from django.http import HttpResponse


def show_form(request):
    return render(request, 'registro.html')

def post_form(request):
    nombre_cancion = request.POST["nombre_cancion"]
    fecha_lanzamiento = request.POST["fecha_lanzamiento"]
    duracion = request.POST["duracion"]
    posicion_ranking = request.POST["posicion_ranking"]
    estilo = request.POST["estilo"]
    interpretes = request.POST["interpretes"]

    return HttpResponse(f"La cancion '{nombre_cancion}' ha sido añadida correctamente")

