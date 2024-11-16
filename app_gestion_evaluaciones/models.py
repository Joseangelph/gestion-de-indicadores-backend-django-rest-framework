from django.db import models
from django.contrib.auth import get_user_model
from app_gestion_plataformas.models import PlataformaTecnologica
from app_gestion_indicadores.models import Indicador

User = get_user_model()  # Obtener el modelo de usuario personalizado

# Create your models here.


class EvaluacionPlataforma(models.Model):
    ESTADOS = [
        ('pendiente a evaluar', 'Pendiente a evaluar'),
        ('pendiente a selección', 'Pendiente a selección'),
        ('evaluada', 'Evaluada'),
    ]
    plataforma = models.ForeignKey(PlataformaTecnologica, on_delete=models.CASCADE)
    estado = models.CharField(max_length=100, choices=ESTADOS, default='pendiente a selección')
    objetivo = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    
class SeleccionIndicador(models.Model):
    evaluacionPlataforma = models.ForeignKey(EvaluacionPlataforma, on_delete=models.CASCADE)
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE)
    fecha_seleccion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('evaluacionPlataforma', 'indicador')  


class EvaluacionIndicador(models.Model):
    EVALUACIONES = [
        ('Sí', 'sí'),
        ('No', 'no'),
    ]
    seleccionIndicador = models.ForeignKey(SeleccionIndicador, on_delete=models.CASCADE)
    observaciones = models.TextField()
    evaluacion = models.CharField(max_length=50, choices=EVALUACIONES)
        
