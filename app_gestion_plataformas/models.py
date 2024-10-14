from django.db import models

# Create your models here.

class PlataformasTecnologicas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    proyecto = models.CharField(max_length=200)
    url = models.TextField()
    alcance = models.CharField(max_length=200)