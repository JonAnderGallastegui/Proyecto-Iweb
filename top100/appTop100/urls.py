from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_estilos.as_view(), name='index'),
    path('estilos/<int:pk>/', views.show_estilos.as_view(), name='detail'),
    path('estilos/<int:estilo_id>/canciones', views.index_canciones.as_view(), name='canciones'),
    path('canciones/<int:pk>', views.show_cancion.as_view(), name='cancion'),
    path('interpretes/<int:interprete_id>', views.show_interpretes.as_view(), name='interprete'),
    path('canciones/', views.index_todas_canciones.as_view(), name='todas_canciones'),
    path('interprete/', views.index_todos_interpretes.as_view(), name='todos_interpretes'),
    path('estilos/', views.index_todos_estilos.as_view(), name='todos_estilos'),
    path('añadir_canciones/', views.show_añadir_canciones, name='añadir_canciones'),
    path('añadidos/', views.show_añadidos, name='añadidos'),
]
