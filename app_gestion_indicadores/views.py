from django.shortcuts import render
from rest_framework import viewsets
from .models import Indicador,CategoriaAnalisis, DestinoImpacto, Componente, Dimension, Subdimension
from .serializers import (IndicadorSerializer,
                          CategoriaAnalisisSerializer, DestinoImpactoSerializer,
                          ComponenteSerializer, DimensionSerializer, SubdimensionSerializer)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrExpertUser


# # Create your views here.

class CategoriaAnalisisViewSet(viewsets.ModelViewSet):
    queryset = CategoriaAnalisis.objects.all()
    serializer_class = CategoriaAnalisisSerializer
    permission_classes = [IsAuthenticated,IsAdminOrExpertUser]

class DestinoImpactoViewSet(viewsets.ModelViewSet):
    queryset = DestinoImpacto.objects.all()
    serializer_class = DestinoImpactoSerializer
    permission_classes = [IsAuthenticated,IsAdminOrExpertUser]

class ComponenteViewSet(viewsets.ModelViewSet):
    queryset = Componente.objects.all()
    serializer_class = ComponenteSerializer
    permission_classes = [IsAuthenticated,IsAdminOrExpertUser]

class DimensionViewSet(viewsets.ModelViewSet):
    queryset = Dimension.objects.all()
    serializer_class = DimensionSerializer
    permission_classes = [IsAuthenticated,IsAdminOrExpertUser]

class SubdimensionViewSet(viewsets.ModelViewSet):
    queryset = Subdimension.objects.all()
    serializer_class = SubdimensionSerializer
    permission_classes = [IsAuthenticated,IsAdminOrExpertUser]

class IndicadorViewSet(viewsets.ModelViewSet):
    queryset = Indicador.objects.all()
    serializer_class = IndicadorSerializer
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated, IsAdminOrExpertUser]
    
    
@api_view(['POST']) 
@permission_classes([IsAuthenticated, IsAdminOrExpertUser])
def toggle_habilitado(request, model_name, pk):
    model_map = {
        'categoria': CategoriaAnalisis,
        'destino': DestinoImpacto,
        'componente': Componente,
        'dimension': Dimension,
        'subdimension': Subdimension,
        'indicador': Indicador,
    }
    
    try:
        model = model_map[model_name]
        instance = model.objects.get(pk=pk)
        instance.habilitado = not instance.habilitado  # Alterna el estado
        instance.save()
        return Response({'status': 'ok', 'habilitado': instance.habilitado})
    except KeyError:
        return Response({'error': 'Modelo no encontrado'}, status=400)
    except model.DoesNotExist:
        return Response({'error': 'Elemento no encontrado'}, status=404)