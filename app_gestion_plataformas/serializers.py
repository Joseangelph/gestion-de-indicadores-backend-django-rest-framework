from rest_framework import serializers
from .models import PlataformaTecnologica

class PlataformasTecnologicasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlataformaTecnologica
        fields = '__all__'