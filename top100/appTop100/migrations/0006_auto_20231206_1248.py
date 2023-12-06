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
        Interprete.objects.create(**interprete_data)

class Migration(migrations.Migration):

    dependencies = [
        ('appTop100', '0005_auto_20231206_1244'),
    ]

    operations = [
        migrations.RunPython(add_initial_interpreters),
    ]
