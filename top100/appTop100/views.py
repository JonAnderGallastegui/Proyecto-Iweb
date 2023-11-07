from django.shortcuts import render

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

#devuelve los detalles de una habilidad
def show_cancion(request, cancion_id):
        cancion = get_object_or_404(Cancion, pk=cancion_id)
        interpretes = cancion.interpretes.all()
        context = { 'cancion': cancion, 'interpretes' : interpretes }
        return render(request, 'cancion.html', context)
