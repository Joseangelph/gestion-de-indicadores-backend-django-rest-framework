from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from django.db import transaction
from django.shortcuts import get_object_or_404
from .models import EvaluacionPlataforma, SeleccionIndicador, EvaluacionIndicador
from app_gestion_indicadores.models import Indicador
from django.contrib.auth import get_user_model
from .serializers import EvaluacionPlataformaSerializer, SeleccionIndicadorSerializer, EvaluacionIndicadorSerializer
from app_gestion_plataformas.serializers import PlataformasTecnologicasSerializer
from django.utils.timezone import now
from app_gestion_indicadores.permissions import IsAdminOrExpertUser
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

class EvaluacionPlataformaViewSet(viewsets.ModelViewSet):
    queryset = EvaluacionPlataforma.objects.all()
    serializer_class = EvaluacionPlataformaSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=True, methods=['patch'])
    def finalizar_evaluacion(self, request, pk=None):
        evaluacion_plataforma = get_object_or_404(EvaluacionPlataforma, pk=pk)
        if evaluacion_plataforma.estado != 'evaluada':
            evaluacion_plataforma.estado = 'evaluada'
            evaluacion_plataforma.fecha_evaluada = now()  # Registrar la fecha de evaluación
            evaluacion_plataforma.save()
            return Response({'message': 'Evaluación finalizada exitosamente.'}, status=status.HTTP_200_OK)
        return Response({'error': 'La evaluación ya estaba en estado evaluada.'}, status=status.HTTP_400_BAD_REQUEST)
       
   
class SeleccionIndicadorViewSet(viewsets.ModelViewSet):
    queryset = SeleccionIndicador.objects.all()
    serializer_class = SeleccionIndicadorSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        evaluacionPlataforma_id = request.data.get('evaluacionPlataformaId')
        indicadores_ids = request.data.get('indicadoresSeleccionados')  # Lista de IDs de indicadores

        # Verificar si ya seleccionó indicadores para esta evaluación
        if SeleccionIndicador.objects.filter(evaluacionPlataforma_id=evaluacionPlataforma_id).exists():
            return Response(
                {'error': 'Ya se ha seleccionado indicadores para esta evaluación.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Crear las selecciones de indicadores
        selecciones = [
            SeleccionIndicador(evaluacionPlataforma_id=evaluacionPlataforma_id, indicador_id=indicador_id)
            for indicador_id in indicadores_ids
        ]
        SeleccionIndicador.objects.bulk_create(selecciones)
        
        # Cambiar el estado de la evaluación de plataforma a "pendiente a evaluación"
        evaluacion_plataforma = get_object_or_404(EvaluacionPlataforma, id=evaluacionPlataforma_id)
        evaluacion_plataforma.estado = 'pendiente a evaluar'
        evaluacion_plataforma.save()

        return Response({'message': 'Selección de indicadores realizada con éxito y estado actualizado a pendiente a evaluación.'}, status=status.HTTP_201_CREATED)

 
class EvaluacionIndicadorViewSet(viewsets.ModelViewSet):
    queryset = EvaluacionIndicador.objects.all()
    serializer_class = EvaluacionIndicadorSerializer
    permission_classes = [IsAuthenticated]

    # Acción personalizada para crear múltiples evaluaciones de indicadores
    @action(detail=False, methods=['post'])
    def crear_evaluaciones(self, request):
        evaluaciones_data = request.data.get('evaluaciones', [])
        evaluaciones_creadas = []
        errores = []

        with transaction.atomic():    
            for evaluacion_data in evaluaciones_data:
                seleccion_id = evaluacion_data.get('seleccionIndicador')
                observaciones = evaluacion_data.get('observaciones')
                evaluacion = evaluacion_data.get('evaluacion')

                # Validar y obtener el objeto de SeleccionIndicador
                seleccion = get_object_or_404(SeleccionIndicador, id=seleccion_id)

                # Crear el objeto de EvaluacionIndicador
                serializer = EvaluacionIndicadorSerializer(data={
                    'seleccionIndicador': seleccion_id,
                    'observaciones': observaciones,
                    'evaluacion': evaluacion,
                })

                if serializer.is_valid():
                    serializer.save()
                    evaluaciones_creadas.append(serializer.data)
                else:
                    errores.append({'seleccion_id': seleccion_id, 'errores': serializer.errors})
                    # transaction.set_rollback(True)  # Deshace la transacción si hay algún error
                    raise ValueError("Error al procesar las evaluaciones.")

        # Enviar la respuesta
        if errores:
            return Response(
                {'evaluaciones_creadas': evaluaciones_creadas, 'errores': errores},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        return Response(
            {'evaluaciones_creadas': evaluaciones_creadas},
            status=status.HTTP_201_CREATED
        )
        
        
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_evaluaciones_por_plataforma(request, plataforma_id):
    """
    Obtiene las evaluaciones de indicadores para una evaluación de plataforma específica.
    """
    try:
        # Filtrar SeleccionIndicador por la evaluación de plataforma dada
        seleccion_indicadores = SeleccionIndicador.objects.filter(evaluacionPlataforma_id=plataforma_id)

        # Filtrar EvaluacionIndicador usando las selecciones de indicadores obtenidas
        evaluaciones = EvaluacionIndicador.objects.filter(seleccionIndicador__in=seleccion_indicadores)

        # Serializar las evaluaciones de indicadores
        serializer = EvaluacionIndicadorSerializer(evaluaciones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"detail": f"Error al obtener evaluaciones: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
    
    
    # evaluaciones = EvaluacionIndicador.objects.filter(seleccionIndicador.evaluacionPlataforma=plataforma_id)
    # serializer = EvaluacionIndicadorSerializer(evaluaciones, many=True)
    # return Response(serializer.data)
    
    
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminOrExpertUser])
def get_plataforma_por_evaluacion(request, evaluacion_id):
    """
    Retorna la plataforma tecnológica asociada a una evaluación específica.
    """
    evaluacion = get_object_or_404(EvaluacionPlataforma, id=evaluacion_id)
    plataforma = evaluacion.plataforma  
    serializer = PlataformasTecnologicasSerializer(plataforma)
    return Response(serializer.data)