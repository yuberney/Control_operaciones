# Generated by Django 4.0.5 on 2024-06-04 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0002_remove_clientes_estado_clientes_activo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='Activo',
            field=models.BooleanField(default=True),
        ),
    ]
