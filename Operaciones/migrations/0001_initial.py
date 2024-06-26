# Generated by Django 4.0.5 on 2024-06-15 15:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Lotes', '0004_alter_lotes_fechaentregado'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Procesos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operaciones',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('FechaRegistro', models.DateField(verbose_name='%Y-%m-%d')),
                ('NumeroOperacionnes', models.IntegerField()),
                ('Precio', models.IntegerField()),
                ('Activo', models.IntegerField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('Lote', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Lotes.lotes')),
                ('Proceso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Procesos.procesos')),
                ('UsuarioResponsable', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Operacion',
                'verbose_name_plural': 'Operaciones',
            },
        ),
    ]
