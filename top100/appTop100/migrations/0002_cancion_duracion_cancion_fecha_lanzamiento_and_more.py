#0002_cancion_duracion_cancion_fecha_lanzamiento_and_more.py

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTop100', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancion',
            name='duracion',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cancion',
            name='fecha_lanzamiento',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='cancion',
            name='posicion',
            field=models.IntegerField(default=0),
        ),
    ]

