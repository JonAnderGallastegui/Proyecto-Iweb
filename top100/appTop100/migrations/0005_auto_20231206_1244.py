# 0005_auto_20231206_1244.py

from django.db import migrations
from datetime import datetime

def add_initial_songs(apps, schema_editor):
    Cancion = apps.get_model('appTop100', 'Cancion')
    Estilo = apps.get_model('appTop100', 'Estilo')
    Interprete = apps.get_model('appTop100', 'Interprete')

    estilo_jazz = Estilo.objects.get(nombre='Jazz')
    interprete_peggy_lee = Interprete.objects.get(nombre='Peggy Lee')
    interprete_michael_buble = Interprete.objects.get(nombre='Michael Bublé')
    interprete_johnny_cash = Interprete.objects.get(nombre='Johnny Cash')
    interprete_adele = Interprete.objects.get(nombre='Adele')
    interprete_ed_sheeran = Interprete.objects.get(nombre='Ed Sheeran')

    canciones_data = [
        {
            'titulo': 'Fever',
            'fecha_lanzamiento': datetime(2023, 12, 5),
            'duracion': 167,
            'posicion': 43,
            'estilo': estilo_jazz,
            'interpretes': [interprete_peggy_lee],
        },
        {
            'titulo': 'Smooth Operator',
            'fecha_lanzamiento': datetime(2023, 12, 6),
            'duracion': 210,
            'posicion': 22,
            'estilo': estilo_jazz,
            'interpretes': [interprete_peggy_lee, interprete_michael_buble],
        },
        {
            'titulo': 'Ring of Fire',
            'fecha_lanzamiento': datetime(2023, 12, 7),
            'duracion': 180,
            'posicion': 30,
            'estilo': Estilo.objects.get(nombre='Country'),
            'interpretes': [interprete_johnny_cash],
        },
   
    ]

    for cancion_data in canciones_data:
        interpretes = cancion_data.pop('interpretes') 
        cancion = Cancion.objects.create(**cancion_data)
        cancion.interpretes.set(interpretes)

class Migration(migrations.Migration):

    dependencies = [
        ('appTop100', '0004_auto_20231205_1630'),
    ]

    operations = [
        migrations.RunPython(add_initial_songs),
    ]
