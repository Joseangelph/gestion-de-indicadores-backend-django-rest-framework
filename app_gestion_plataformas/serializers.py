from rest_framework import serializers
from .models import PlataformasTecnologicas

class PlataformasTecnologicasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlataformasTecnologicas
        fields = '__all__'