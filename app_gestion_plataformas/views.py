from django.shortcuts import render
from .models import PlataformasTecnologicas
from .serializers import PlataformasTecnologicasSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class PlataformasTecnologicasViewSet(viewsets.ModelViewSet):
    queryset = PlataformasTecnologicas.objects.all()
    serializer_class = PlataformasTecnologicasSerializer
    permission_classes = [IsAuthenticated]