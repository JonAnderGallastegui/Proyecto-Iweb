from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Estilo, Interprete, Cancion
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, get_list_or_404


class index_estilos(ListView):
    model = Cancion
    template_name = 'index.html'
    context_object_name = 'lista_canciones'
    queryset = Cancion.objects.raw('SELECT * FROM (SELECT * FROM appTop100_Cancion ORDER BY posicion ASC) GROUP BY estilo_id')

""" def index_estilos(request):
        canciones = Cancion.objects.raw('SELECT * FROM (SELECT * FROM appTop100_Cancion ORDER BY posicion ASC) GROUP BY estilo_id')
        context = {'lista_canciones': canciones }
        return render(request, 'index.html', context) """

class show_estilos(DetailView):
    model = Estilo
    template_name = 'detail.html'
    context_object_name = 'estilo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

""" #devuelve los datos de un estilo
def show_estilos(request, estilo_id):
        estilo = get_object_or_404(Estilo, pk=estilo_id)
        context = {'estilo': estilo }
        return render(request, 'detail.html', context) """


class show_interpretes(ListView):
    model = Cancion
    template_name = 'interprete.html'
    context_object_name = 'canciones'

    def get_queryset(self):
        interprete_id = self.kwargs['interprete_id']
        interprete = get_object_or_404(Interprete, pk=interprete_id)
        return interprete.cancion_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        interprete_id = self.kwargs['interprete_id']
        interprete = get_object_or_404(Interprete, pk=interprete_id)
        context['interprete'] = interprete
        return context

""" #devuelve los detalles de un interprete
def show_interpretes(request, interprete_id):
        interprete = get_object_or_404(Interprete, pk=interprete_id)
        canciones =  interprete.cancion_set.all()
        context = { 'canciones': canciones, 'interprete' : interprete }
        return render(request, 'interprete.html', context) """

class index_canciones(ListView):
    model = Cancion
    template_name = 'canciones.html'
    context_object_name = 'canciones'

    def get_queryset(self):
        estilo_id = self.kwargs['estilo_id']
        estilo = get_object_or_404(Estilo, pk=estilo_id)
        return estilo.cancion_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        estilo_id = self.kwargs['estilo_id']
        estilo = get_object_or_404(Estilo, pk=estilo_id)
        context['estilo'] = estilo
        return context

""" #devuelve los detalles de una cancion
def index_canciones(request, estilo_id):
        estilo = get_object_or_404(Estilo, pk=estilo_id)
        canciones =  estilo.cancion_set.all()
        context = {'estilo': estilo, 'canciones' : canciones }
        return render(request, 'canciones.html', context) """

class show_cancion(DetailView):
    model = Cancion
    template_name = 'cancion.html'
    context_object_name = 'cancion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['interpretes'] = self.object.interpretes.all()
        return context


""" #devuelve los detalles de una cancion
def show_cancion(request, cancion_id):
        cancion = get_object_or_404(Cancion, pk=cancion_id)
        interpretes = cancion.interpretes.all()
        context = { 'cancion': cancion, 'interpretes' : interpretes }
        return render(request, 'cancion.html', context) """

class index_todas_canciones(ListView):
      model = Cancion
      template_name = 'todasCanciones.html'
      context_object_name = 'canciones'
      ordering = ['titulo']

""" def index_todas_canciones(request):
    canciones = get_list_or_404(Cancion.objects.order_by('titulo'))
    context = {'canciones': canciones}
    return render(request, 'todasCanciones.html', context) """

class index_todos_interpretes(ListView):
      model = Interprete
      template_name = 'todosInterpretes.html'
      context_object_name = 'interpretes'
      ordering = ['nombre']

""" # En tu vista
def index_todos_interpretes(request):
    interpretes = get_list_or_404(Interprete.objects.order_by('nombre'))
    context = {'interpretes': interpretes}
    return render(request, 'todosInterpretes.html', context) """

class index_todos_estilos(ListView):
    model = Estilo
    template_name = 'todosEstilos.html'
    context_object_name = 'lista_estilos'
    ordering = ['nombre']


""" def index_todos_estilos(request):
        estilos  = get_list_or_404(Estilo.objects.order_by('nombre'))
        context = {'lista_estilos': estilos }
        return render(request, 'todosEstilos.html', context)

 """
def show_añadir_canciones(request):
    return render(request, 'añadir_canciones.html')
from django.shortcuts import redirect


def show_añadidos(request):
    if request.method == 'POST':
        nombre_cancion = request.POST.get("nombre_cancion")
        fecha_lanzamiento = request.POST.get("fecha_lanzamiento")
        duracion = request.POST.get("duracion")
        posicion_ranking = request.POST.get("posicion_ranking")
        estilo_nombre = request.POST.get("estilo")
        interpretes_nombres = request.POST.get("interpretes")

        if not nombre_cancion or not fecha_lanzamiento or not duracion or not posicion_ranking or not estilo_nombre or not interpretes_nombres:
            return HttpResponse("Error: Todos los campos son obligatorios")

        try:
            duracion = int(duracion)
            posicion_ranking = int(posicion_ranking)
        except ValueError:
            return HttpResponse("Error: La duración y la posición en el ranking deben ser números enteros")

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
