from django.db import models

# Create your models here.

class CategoriaAnalisis(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    concepto = models.TextField(null=True)

class DestinoImpacto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    categoria_analisis = models.ForeignKey(CategoriaAnalisis, on_delete=models.CASCADE)
    concepto = models.TextField(null=True)

class Componente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    destino_impacto = models.ForeignKey(DestinoImpacto, on_delete=models.CASCADE, null=True, blank=True)
    concepto = models.TextField(null=True)

class Dimension(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    destino_impacto = models.ForeignKey(DestinoImpacto, on_delete=models.CASCADE, null=True, blank=True)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE, null=True, blank=True)
    concepto = models.TextField(null=True)

class Subdimension(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE, null=True, blank=True)
    concepto = models.TextField(null=True)

class Indicador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    concepto = models.TextField()
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE, null=True, blank=True)
    subdimension = models.ForeignKey(Subdimension, on_delete=models.CASCADE, null=True, blank=True)
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre