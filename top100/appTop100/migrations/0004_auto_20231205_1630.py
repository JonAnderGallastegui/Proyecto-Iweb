#0004_auto_20231205_1630.py

from django.db import migrations

def add_initial_data(apps, schema_editor):
    Estilo = apps.get_model('appTop100', 'Estilo')

    estilos_data = [
        'Funk',
        'Reggae',
        'Country',
        'Electronic',
        'Classical',
    ]

    for estilo_nombre in estilos_data:
        Estilo.objects.create(nombre=estilo_nombre)

class Migration(migrations.Migration):

    dependencies = [
        ('appTop100', '0003_alter_interprete_fecha_nacimiento'),
    ]

    operations = [
        migrations.RunPython(add_initial_data),
    ]













