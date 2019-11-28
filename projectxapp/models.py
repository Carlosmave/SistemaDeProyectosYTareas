from django.db import models
from datetime import datetime

# Create your models here.

#General Models

class Tarea(models.Model):
    titulo = models.CharField(max_length=500)
    descripcion = models.CharField(max_length=500)
    avance = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name_plural = "Tareas"
        ordering = ['-id']

class Proyecto(models.Model):
    nombre = models.CharField(max_length=500)
    descripcion = models.CharField(max_length=500)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Proyectos"
        ordering = ['-id']

#
# class Proyecto(models.Model):
#
#     nombre_proyecto = models.CharField(max_length=50)
#     arquitecto = models.TextField()
#     fecha_creacion = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         app_label: 'app'
#
#
# class Tarea(models.Model):
#
#     titulo = models.CharField(max_length = 100 )
#     desarrolladores = models.TextField()
#     fecha_creacion = models.DateTimeField(auto_now_add=True)
#     activo = models.BooleanField()
#     proyecto = models.ForeignKey(
#         Proyecto,
#         related_name='tarea',
#         on_delete = models.CASCADE,
#         null = False
#     )
#
#     class Meta:
#         app_label: 'app'
