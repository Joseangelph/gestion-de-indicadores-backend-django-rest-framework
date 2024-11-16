from django.test import TestCase
from .models import CategoriaAnalisis, DestinoImpacto, Componente, Dimension, Subdimension, Indicador
from .serializers import IndicadorSerializer

class TestIndicadorGetDimensionNombre(TestCase):
    def setUp(self):
        # Crear instancias de modelos relacionadas necesarias para las pruebas
        self.categoria_analisis = CategoriaAnalisis.objects.create(nombre="Categoría de Análisis")
        self.destino_impacto = DestinoImpacto.objects.create(nombre="Destino de Impacto", categoria_analisis=self.categoria_analisis)
        self.componente = Componente.objects.create(nombre="Componente", destino_impacto=self.destino_impacto)
        self.dimension = Dimension.objects.create(nombre="Dimensión", destino_impacto=self.destino_impacto, componente=self.componente)
        self.subdimension = Subdimension.objects.create(nombre="Subdimensión", dimension=self.dimension)
        
    def test_get_dimension_nombre_with_subdimension_and_dimension(self):
        # Caso 1: El indicador tiene subdimension y subdimension tiene dimension
        indicador = Indicador.objects.create(nombre="Indicador 1", concepto="Concepto", subdimension=self.subdimension)
        serializer = IndicadorSerializer(indicador)
        self.assertEqual(serializer.data['dimension_nombre'], "Dimensión")

    def test_get_dimension_nombre_without_subdimension_with_dimension(self):
        # Caso 2: El indicador no tiene subdimension, pero tiene dimension
        indicador = Indicador.objects.create(nombre="Indicador 2", concepto="Concepto", dimension=self.dimension)
        serializer = IndicadorSerializer(indicador)
        self.assertEqual(serializer.data['dimension_nombre'], "Dimensión")

    # def test_get_dimension_nombre_with_subdimension_without_dimension(self):
    #     # Caso 2: El indicador tiene subdimension, pero subdimension no tiene dimension
    #     subdimension_no_dimension = Subdimension.objects.create(nombre="Subdimensión sin dimensión", dimension=None)
    #     indicador = Indicador.objects.create(nombre="Indicador 2", concepto="Concepto", subdimension=subdimension_no_dimension)
    #     serializer = IndicadorSerializer(indicador)
    #     self.assertEqual(serializer.data['dimension_nombre'], "")  # Esperamos una cadena vacía
    
    
    # def test_get_dimension_nombre_without_subdimension_and_dimension(self):
    #     # Caso 4: El indicador no tiene subdimension ni dimension
    #     indicador = Indicador.objects.create(nombre="Indicador 4", concepto="Concepto")
    #     serializer = IndicadorSerializer(indicador)
    #     self.assertEqual(serializer.data['dimension_nombre'], "")  # Esperamos una cadena vacía