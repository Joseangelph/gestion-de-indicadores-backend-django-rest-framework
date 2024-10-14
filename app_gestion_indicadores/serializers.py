from rest_framework import serializers
from .models import Indicador
from .models import CategoriaAnalisis, DestinoImpacto, Componente, Dimension, Subdimension


class CategoriaAnalisisSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaAnalisis
        fields = '__all__'
        

class DestinoImpactoSerializer(serializers.ModelSerializer):
    categoria_analisis_nombre = serializers.CharField(source='categoria_analisis.nombre', read_only=True)

    class Meta:
        model = DestinoImpacto
        fields = ['id', 'nombre', 'concepto', 'categoria_analisis', 'categoria_analisis_nombre']
        
        
class ComponenteSerializer(serializers.ModelSerializer):
    destino_impacto_nombre = serializers.CharField(source='destino_impacto.nombre', read_only=True)

    class Meta:
        model = Componente
        fields = ['id', 'nombre', 'concepto', 'destino_impacto', 'destino_impacto_nombre']
        
        
class DimensionSerializer(serializers.ModelSerializer):    
    componente_nombre = serializers.SerializerMethodField()
    destino_impacto_nombre = serializers.SerializerMethodField()

    class Meta:
        model = Dimension
        fields = ['id', 'nombre', 'concepto', 'destino_impacto', 'destino_impacto_nombre', 'componente', 'componente_nombre']
        
    def get_componente_nombre(self, obj):
        """Retorna el nombre del componente si existe, de lo contrario devuelve una cadena vacía."""
        return obj.componente.nombre if obj.componente else ""
    
    def get_destino_impacto_nombre(self, obj):
        """Obtiene el destino de impacto según si la dimensión tiene componente o no."""
        if obj.componente:
            return obj.componente.destino_impacto.nombre if obj.componente.destino_impacto else ""
        return obj.destino_impacto.nombre if obj.destino_impacto else ""


class SubdimensionSerializer(serializers.ModelSerializer):
    dimension_nombre = serializers.CharField(source='dimension.nombre', read_only=True)

    class Meta:
        model = Subdimension
        fields = ['id', 'nombre', 'concepto', 'dimension', 'dimension_nombre']


class IndicadorSerializer(serializers.ModelSerializer):
    dimension_nombre = serializers.SerializerMethodField()
    subdimension_nombre = serializers.SerializerMethodField()
    
    class Meta:
        model = Indicador
        fields = ['id', 'nombre', 'concepto', 'tipo', 'dimension', 'subdimension', 'subdimension_nombre', 'dimension_nombre']
    
    def get_subdimension_nombre(self, obj):
        """Retorna el nombre de la subdimensión si existe, de lo contrario devuelve una cadena vacía."""
        return obj.subdimension.nombre if obj.subdimension else ""
    
    def get_dimension_nombre(self, obj):
        """Obtiene la dimensión según si el indicador tiene subdimension o no."""
        if obj.subdimension:
            return obj.subdimension.dimension.nombre if obj.subdimension.dimension else ""
        return obj.dimension.nombre if obj.dimension else ""