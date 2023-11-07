from django.contrib import admin

# Register your models here.
from .models import Estilo, Interprete, Cancion
admin.site.register(Estilo)
admin.site.register(Interprete)
admin.site.register(Cancion)
