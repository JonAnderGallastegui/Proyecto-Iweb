# 0006_auto_20231206_1248.py

from django.db import migrations

def add_initial_interpreters(apps, schema_editor):
    Interprete = apps.get_model('appTop100', 'Interprete')

    interpretes_data = [
        {
            'nombre': 'Adele',
            'fecha_nacimiento': '1988-05-05',

        },
        {
            'nombre': 'Ed Sheeran',
            'fecha_nacimiento': '1991-02-17',

        },
   
    ]

    for interprete_data in interpretes_data:
        foto_path = interprete_data.pop('foto')  
        interprete = Interprete.objects.create(**interprete_data)
        interprete.foto = foto_path
        interprete.save()

class Migration(migrations.Migration):

    dependencies = [
        ('appTop100', '0005_auto_20231206_1244'),
    ]

    operations = [
        migrations.RunPython(add_initial_interpreters),
    ]
