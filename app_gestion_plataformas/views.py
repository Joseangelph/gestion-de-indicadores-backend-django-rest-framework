from django.shortcuts import render
from .models import PlataformaTecnologica
from .serializers import PlataformasTecnologicasSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class PlataformasTecnologicasViewSet(viewsets.ModelViewSet):
    queryset = PlataformaTecnologica.objects.all()
    serializer_class = PlataformasTecnologicasSerializer
    permission_classes = [IsAuthenticated]