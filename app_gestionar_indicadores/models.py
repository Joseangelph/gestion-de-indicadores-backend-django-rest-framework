from django.db import models

# Create your models here.

class Indicador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    # valor = models.DecimalField(max_digits=10, decimal_places=2)
    # fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre