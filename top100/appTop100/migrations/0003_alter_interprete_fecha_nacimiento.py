#0003_alter_interprete_fecha_nacimiento.py

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTop100', '0002_cancion_duracion_cancion_fecha_lanzamiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interprete',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
