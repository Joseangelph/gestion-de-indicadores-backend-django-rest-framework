from rest_framework import serializers
from .models import EvaluacionPlataforma, SeleccionIndicador, EvaluacionIndicador
from django.contrib.auth import get_user_model
from app_gestion_indicadores.models import Indicador

User = get_user_model()  # Obtener el modelo de usuario actual (CustomUser)

class EvaluacionPlataformaSerializer(serializers.ModelSerializer):
    plataforma_nombre = serializers.CharField(source='plataforma.nombre', read_only=True)
    
    class Meta:
        model = EvaluacionPlataforma
        fields = ['id','plataforma', 'estado', 'objetivo','fecha_creacion', 'fecha_actualizacion', 'plataforma_nombre']
        
        
class SeleccionIndicadorSerializer(serializers.ModelSerializer):
    indicador_nombre = serializers.CharField(source='indicador.nombre', read_only=True)
    class Meta:
        model = SeleccionIndicador
        fields = ['id','evaluacionPlataforma', 'indicador', 'fecha_seleccion','indicador_nombre']
        

class EvaluacionIndicadorSerializer(serializers.ModelSerializer):
    indicador_nombre = serializers.SerializerMethodField()
    
    def get_indicador_nombre(self, obj):
        return obj.seleccionIndicador.indicador.nombre
    
    class Meta:
        model = EvaluacionIndicador
        fields = ['id', 'seleccionIndicador', 'observaciones', 'evaluacion', 'indicador_nombre']