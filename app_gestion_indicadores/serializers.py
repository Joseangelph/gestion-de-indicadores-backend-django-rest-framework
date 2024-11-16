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
        fields = ['id', 'nombre', 'concepto', 'habilitado' ,'categoria_analisis', 'categoria_analisis_nombre']
        
        
class ComponenteSerializer(serializers.ModelSerializer):
    destino_impacto_nombre = serializers.CharField(source='destino_impacto.nombre', read_only=True)

    class Meta:
        model = Componente
        fields = ['id', 'nombre', 'concepto', 'habilitado', 'destino_impacto', 'destino_impacto_nombre']
        
        
class DimensionSerializer(serializers.ModelSerializer):    
    componente_nombre = serializers.SerializerMethodField()
    destino_impacto_nombre = serializers.SerializerMethodField()

    class Meta:
        model = Dimension
        fields = ['id', 'nombre', 'concepto', 'habilitado','destino_impacto', 'destino_impacto_nombre', 'componente', 'componente_nombre']
        
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
        fields = ['id', 'nombre', 'concepto', 'habilitado', 'dimension', 'dimension_nombre']


class IndicadorSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.SerializerMethodField()
    destino_nombre = serializers.SerializerMethodField()
    componente_nombre = serializers.SerializerMethodField()
    dimension_nombre = serializers.SerializerMethodField()
    subdimension_nombre = serializers.SerializerMethodField()
    
    class Meta:
        model = Indicador
        fields = ['id', 'nombre', 'concepto', 'habilitado', 'tipo',
                  'dimension', 'subdimension', 'subdimension_nombre',
                  'dimension_nombre','componente_nombre','destino_nombre',
                  'categoria_nombre']
    
    def get_subdimension_nombre(self, obj):
        """Retorna el nombre de la subdimensión si existe, de lo contrario devuelve una cadena vacía."""
        return obj.subdimension.nombre if obj.subdimension else ""
    
    # def get_dimension_nombre(self, obj):
    #     """Obtiene la dimensión según si el indicador tiene subdimension o no."""
    #     if obj.subdimension: #1
    #         return obj.subdimension.dimension.nombre if obj.subdimension.dimension else ""  #2  #3
    #     return obj.dimension.nombre if obj.dimension else ""          #4 #5
    
    
    # def get_dimension_nombre(self, obj):
    #     """Obtiene la dimensión según si el indicador tiene subdimension o no."""
    #     if obj.subdimension: #1
    #         if obj.subdimension.dimension:  #2
    #             return obj.subdimension.dimension.nombre #3
    #         return ""  #4
    #     if obj.dimension:  #5
    #         return obj.dimension.nombre    #6
    #     return ""   #7
    
    
    def get_dimension_nombre(self, obj):
        """Obtiene la dimensión según si el indicador tiene subdimension o no."""
        if obj.subdimension: #1
                return obj.subdimension.dimension.nombre #2
        elif obj.dimension:  #3
            return obj.dimension.nombre    #4
    
    
    def get_componente_nombre(self, obj):
        if obj.subdimension:
            return obj.subdimension.dimension.componente.nombre if obj.subdimension.dimension.componente else ""
        return obj.dimension.componente.nombre if obj.dimension.componente else ""
   
    def get_destino_nombre(self, obj):
        if obj.subdimension:
            if obj.subdimension.dimension.componente:
                return obj.subdimension.dimension.componente.destino_impacto.nombre
            return obj.subdimension.dimension.destino_impacto.nombre
        if obj.dimension:
            if obj.dimension.componente:
                return obj.dimension.componente.destino_impacto.nombre
            return obj.dimension.destino_impacto.nombre
    
    def get_categoria_nombre(self, obj):
        if obj.subdimension:
            if obj.subdimension.dimension.componente:
                return obj.subdimension.dimension.componente.destino_impacto.categoria_analisis.nombre
            return obj.subdimension.dimension.destino_impacto.categoria_analisis.nombre
        if obj.dimension:
            if obj.dimension.componente:
                return obj.dimension.componente.destino_impacto.categoria_analisis.nombre
            return obj.dimension.destino_impacto.categoria_analisis.nombre
        
        
    
     # def get_componente_nombre(self, obj):
    #     if obj.subdimension and obj.subdimension.dimension:
    #         return obj.subdimension.dimension.componente.nombre if obj.subdimension.dimension.componente else ""
    #     return obj.dimension.componente.nombre if obj.dimension and obj.dimension.componente else ""
    
    # def get_destino_nombre(self, obj):
    #     if obj.subdimension and obj.subdimension.dimension and obj.subdimension.dimension.componente:
    #         return obj.subdimension.dimension.componente.destino.nombre if obj.subdimension.dimension.componente.destino else ""
    #     if obj.dimension and obj.dimension.componente:
    #         return obj.dimension.componente.destino.nombre if obj.dimension.componente.destino else ""
    #     return ""
    
    # def get_categoria_nombre(self, obj):
    #     if obj.subdimension and obj.subdimension.dimension and obj.subdimension.dimension.componente and obj.subdimension.dimension.componente.destino:
    #         return obj.subdimension.dimension.componente.destino.categoria.nombre if obj.subdimension.dimension.componente.destino.categoria else ""
    #     if obj.dimension and obj.dimension.componente and obj.dimension.componente.destino:
    #         return obj.dimension.componente.destino.categoria.nombre if obj.dimension.componente.destino.categoria else ""
    #     return ""
    

            