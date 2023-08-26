# Generated by Django 4.2.3 on 2023-08-12 01:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tareasDjango', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comentarioTarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(blank=True, max_length=512, null=True)),
                ('tareaRelacionado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tareasDjango.tareasinformacion')),
                ('usuarioRelacionado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
