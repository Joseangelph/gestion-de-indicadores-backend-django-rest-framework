from django.shortcuts import render
from rest_framework import viewsets
from .models import Indicador,CategoriaAnalisis, DestinoImpacto, Componente, Dimension, Subdimension
from .serializers import (IndicadorSerializer,
                          CategoriaAnalisisSerializer, DestinoImpactoSerializer,
                          ComponenteSerializer, DimensionSerializer, SubdimensionSerializer)
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

# # Create your views here.

class CategoriaAnalisisViewSet(viewsets.ModelViewSet):
    queryset = CategoriaAnalisis.objects.all()
    serializer_class = CategoriaAnalisisSerializer
    permission_classes = [IsAuthenticated]

class DestinoImpactoViewSet(viewsets.ModelViewSet):
    queryset = DestinoImpacto.objects.all()
    serializer_class = DestinoImpactoSerializer
    permission_classes = [IsAuthenticated]

class ComponenteViewSet(viewsets.ModelViewSet):
    queryset = Componente.objects.all()
    serializer_class = ComponenteSerializer
    permission_classes = [IsAuthenticated]

class DimensionViewSet(viewsets.ModelViewSet):
    queryset = Dimension.objects.all()
    serializer_class = DimensionSerializer
    permission_classes = [IsAuthenticated]

class SubdimensionViewSet(viewsets.ModelViewSet):
    queryset = Subdimension.objects.all()
    serializer_class = SubdimensionSerializer
    permission_classes = [IsAuthenticated]

class IndicadorViewSet(viewsets.ModelViewSet):
    queryset = Indicador.objects.all()
    serializer_class = IndicadorSerializer
    permission_classes = [IsAuthenticated]