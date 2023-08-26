from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class datosUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    tipoUsuario = models.CharField(max_length=16,null=True, blank=True)
    nroCelular = models.CharField(max_length=16,null=True, blank=True)
    profesionUsuario = models.CharField(max_length=32,null=True, blank=True)
    perfilUsuario = models.CharField(max_length=512,null=True, blank=True)
    fechaIngreso = models.DateField(null=True)

class tareasInformacion(models.Model):
    usuarioRelacionado = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcionTarea = models.CharField(max_length=512,null=True, blank=True)
    fechaInicio = models.DateField(null=True)
    fechaFin = models.DateField(null=True)
    estadoTarea = models.CharField(max_length=16,null=True, blank=True)

class comentarioTarea(models.Model):
    tareaRelacionado = models.ForeignKey(tareasInformacion, on_delete=models.CASCADE)
    usuarioRelacionado = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=512, null=True, blank=True) 