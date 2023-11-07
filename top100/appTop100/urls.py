from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_estilos, name='index'),
    path('estilos/<int:estilo_id>/', views.show_estilos, name='detail'),
    path('estilos/<int:estilo_id>/canciones', views.index_canciones, name='canciones'),
    path('canciones/<int:cancion_id>', views.show_cancion, name='cancion'),
    path('interpretes/<int:interprete_id>', views.show_interpretes, name='interprete'),
]
