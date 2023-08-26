# Generated by Django 4.2.4 on 2023-08-05 01:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='tareasInformacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcionTarea', models.CharField(blank=True, max_length=512, null=True)),
                ('fechaInicio', models.DateField(null=True)),
                ('fechaFin', models.DateField(null=True)),
                ('estadoTarea', models.CharField(blank=True, max_length=16, null=True)),
                ('usuarioRelacionado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='datosUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoUsuario', models.CharField(blank=True, max_length=16, null=True)),
                ('nroCelular', models.CharField(blank=True, max_length=16, null=True)),
                ('profesionUsuario', models.CharField(blank=True, max_length=32, null=True)),
                ('perfilUsuario', models.CharField(blank=True, max_length=512, null=True)),
                ('fechaIngreso', models.DateField(null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
