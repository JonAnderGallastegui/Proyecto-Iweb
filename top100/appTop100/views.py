from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Estilo, Interprete, Cancion
from django.shortcuts import get_object_or_404, get_list_or_404

#devuelve el listado de estilos
def index_estilos(request):
        estilos  = get_list_or_404(Estilo.objects.order_by('nombre'))
        context = {'lista_estilos': estilos }
        return render(request, 'index.html', context)

#devuelve los datos de un estilo
def show_estilos(request, estilo_id):
        estilo = get_object_or_404(Estilo, pk=estilo_id)
        context = {'estilo': estilo }
        return render(request, 'detail.html', context)

#devuelve los detalles de un interprete
def show_interpretes(request, interprete_id):
        interprete = get_object_or_404(Interprete, pk=interprete_id)
        canciones =  interprete.cancion_set.all()
        context = { 'canciones': canciones, 'interprete' : interprete }
        return render(request, 'interprete.html', context)

#devuelve los detalles de una cancion
def index_canciones(request, estilo_id):
        estilo = get_object_or_404(Estilo, pk=estilo_id)
        canciones =  estilo.cancion_set.all()
        context = {'estilo': estilo, 'canciones' : canciones }
        return render(request, 'canciones.html', context)

#devuelve los detalles de una cancion
def show_cancion(request, cancion_id):
        cancion = get_object_or_404(Cancion, pk=cancion_id)
        interpretes = cancion.interpretes.all()
        context = { 'cancion': cancion, 'interpretes' : interpretes }
        return render(request, 'cancion.html', context)

def index_todas_canciones(request):
    canciones = get_list_or_404(Cancion.objects.order_by('titulo'))
    context = {'canciones': canciones}
    return render(request, 'todasCanciones.html', context)

# En tu vista
def index_todos_interpretes(request):
    interpretes = get_list_or_404(Interprete.objects.order_by('nombre'))
    context = {'interpretes': interpretes}
    return render(request, 'todosInterpretes.html', context)

#devuelve el listado de estilos
def index_todos_estilos(request):
        estilos  = get_list_or_404(Estilo.objects.order_by('nombre'))
        context = {'lista_estilos': estilos }
        return render(request, 'todosEstilos.html', context)


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

