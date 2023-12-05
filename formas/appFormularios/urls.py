from django.urls import path
from . import views
urlpatterns = [
    path('registro/', views.show_form, name='registro'),
    path('registrar/', views.post_form, name='registrar')
]