from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Estilo, Interprete, Cancion


#devuelve el listado de estilos
def index_estilos(request):
	estilos = Estilo.objects.order_by('nombre')
	output = ', '.join([e.nombre for e in estilos])
	return HttpResponse(output)

#devuelve los datos de un estilo
def show_estilos(request, estilo_id):
	estilo = Estilo.objects.get(pk=estilo_id)
	output = f'Detalles del estilo: {estilo.id}, {estilo.nombre}'
	return HttpResponse(output)

#devuelve los detalles de un interprete
def show_interpretes(request, interprete_id):
	interprete = Interprete.objects.get(pk=interprete_id)
	output = f'Detalles del Interprete: {interprete.id}, {interprete.nombre}, {interprete.fecha_nacimiento}. Canciones: {[c.nombre for c in interprete.cancion_set.all()]}'
	return HttpResponse(output)


#devuelve los detalles de una cancion
def index_canciones(request, estilo_id):
        estilo = Estilo.objects.get(pk=estilo_id)
        output = ', '.join([c.titulo for c in estilo.cancion_set.all()])  
        return HttpResponse(output)

#devuelve los detalles de una habilidad
def show_cancion(request, cancion_id):
	cancion = Cancion.objects.get(pk=cancion_id)
	output = f'Detalles de la cancion: {cancion.id}, {cancion.titulo}, {str(cancion.estilo)}. Interpretes: {[i.nombre for i in cancion.interpretes.all()]}'
	return HttpResponse(output)
