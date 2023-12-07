#0007_interprete_foto.py

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTop100', '0006_auto_20231206_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='interprete',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/'),
        ),
    ]
