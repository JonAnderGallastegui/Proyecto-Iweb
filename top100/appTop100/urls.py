
from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
 path('departamento/<int:departamento_id>', views.detail, name='detail'),
 path('departamento/<int:departamento_id>/empleados', views.empleados, name='empleados'),
 path('empleado/<int:empleado_id>', views.empleado, name='empleado'),
 path('habilidad/<int:habilidad_id>', views.habilidad, name='habilidad')
]