from django.db import models

# Create your models here.

class CategoriaAnalisis(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=1000)
    concepto = models.TextField(null=True)
    habilitado = models.BooleanField(default=True)

class DestinoImpacto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=1000)
    categoria_analisis = models.ForeignKey(CategoriaAnalisis, on_delete=models.CASCADE)
    concepto = models.TextField(null=True)
    habilitado = models.BooleanField(default=True)

class Componente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=1000)
    destino_impacto = models.ForeignKey(DestinoImpacto, on_delete=models.CASCADE, null=True, blank=True)
    concepto = models.TextField(null=True)
    habilitado = models.BooleanField(default=True)

class Dimension(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=1000)
    destino_impacto = models.ForeignKey(DestinoImpacto, on_delete=models.CASCADE, null=True, blank=True)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE, null=True, blank=True)
    concepto = models.TextField(null=True)
    habilitado = models.BooleanField(default=True)

class Subdimension(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=1000)
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE, null=True, blank=True)
    concepto = models.TextField(null=True)
    habilitado = models.BooleanField(default=True)

class Indicador(models.Model):
    TIPOS = (
        ('potencial', 'Potencial'),
        ('transversal', 'Transversal'),
        ('real', 'Real'),
    )
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=1000)
    concepto = models.TextField()
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE, null=True, blank=True)
    subdimension = models.ForeignKey(Subdimension, on_delete=models.CASCADE, null=True, blank=True)
    tipo = models.CharField(max_length=50, choices=TIPOS)
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre