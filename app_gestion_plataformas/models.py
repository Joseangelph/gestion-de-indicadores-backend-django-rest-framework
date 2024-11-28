from django.db import models

# Create your models here.

class PlataformaTecnologica(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, unique= True)
    descripcion = models.TextField()
    proyecto = models.CharField(max_length=255)
    url = models.URLField()
    alcance = models.CharField(max_length=255)
    habilitado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre