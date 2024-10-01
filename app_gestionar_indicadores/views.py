from django.shortcuts import render
from rest_framework import viewsets
from .models import Indicador
from .serializers import IndicadorSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

# Create your views here.



class IndicadorViewSet(viewsets.ModelViewSet):
    queryset = Indicador.objects.all()
    serializer_class = IndicadorSerializer
    permission_classes = [IsAuthenticated]