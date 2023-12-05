from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_estilos, name='index'),
    path('switch-language/<str:language_code>/', views.switch_language, name='switch_language'),
    path('estilos/<int:estilo_id>/', views.show_estilos, name='detail'),
    path('estilos/<int:estilo_id>/canciones', views.index_canciones, name='canciones'),
    path('canciones/<int:cancion_id>', views.show_cancion, name='cancion'),
    path('interpretes/<int:interprete_id>', views.show_interpretes, name='interprete'),
    path('canciones/', views.index_todas_canciones, name='todas_canciones'),
    path('interprete/', views.index_todos_interpretes, name='todos_interpretes'),
    path('estilos/', views.index_todos_estilos.as_view(), name='todos_estilos'),
    path('añadir_canciones/', views.show_añadir_canciones, name='añadir_canciones'),
    path('añadidos/', views.show_añadidos, name='añadidos'),
]
