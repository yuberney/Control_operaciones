# Generated by Django 4.0.5 on 2024-06-02 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Documento',
            field=models.IntegerField(null=True, unique=True, verbose_name='Documento'),
        ),
    ]
