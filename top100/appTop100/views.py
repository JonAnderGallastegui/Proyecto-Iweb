from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Estilo, Interprete, Cancion


# Create your views here.
from .models import Estilo, Interprete, Cancion
from django.shortcuts import get_object_or_404, get_list_or_404

#devuelve el listado de estilos
def index_estilos(request):
        canciones = Cancion.objects.raw('SELECT * FROM (SELECT * FROM appTop100_Cancion ORDER BY posicion ASC) GROUP BY estilo_id')
        context = {'lista_canciones': canciones }
        return render(request, 'index.html', context)

from django.shortcuts import redirect
from django.utils.translation import activate


def switch_language(request, language_code):
    # Activate the chosen language
    activate(language_code)

    print(f'Activated language: {language_code}')

    # Redirect to the previous page or a default page
    return redirect(request.META.get('HTTP_REFERER', '/'))




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


def show_añadir_canciones(request):
    return render(request, 'añadir_canciones.html')
from django.shortcuts import redirect

def show_añadidos(request):
    if request.method == 'POST':
        nombre_cancion = request.POST["nombre_cancion"]
        fecha_lanzamiento = request.POST["fecha_lanzamiento"]
        duracion = request.POST["duracion"]
        posicion_ranking = request.POST["posicion_ranking"]
        estilo_nombre = request.POST["estilo"]
        interpretes_nombres = request.POST["interpretes"]

        estilo, creado = Estilo.objects.get_or_create(nombre=estilo_nombre)

        interpretes_nombres = interpretes_nombres.split(',')
        interpretes = [Interprete.objects.get_or_create(nombre=nombre.strip())[0] for nombre in interpretes_nombres]

        nueva_cancion = Cancion(
            titulo=nombre_cancion,
            estilo=estilo,
            fecha_lanzamiento=fecha_lanzamiento,
            duracion=duracion,
            posicion=posicion_ranking
        )
        nueva_cancion.save()

        nueva_cancion.interpretes.set(interpretes)

        return redirect('todas_canciones')  

    return HttpResponse("Error: Método no permitido")
