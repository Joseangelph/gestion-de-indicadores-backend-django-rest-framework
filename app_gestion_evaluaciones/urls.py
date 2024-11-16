from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EvaluacionPlataformaViewSet,SeleccionIndicadorViewSet,EvaluacionIndicadorViewSet
from .views import get_evaluaciones_por_plataforma

router = DefaultRouter()
router.register(r'evaluacionesplataformas', EvaluacionPlataformaViewSet)
router.register(r'evaluacionesindicadores', EvaluacionIndicadorViewSet)
router.register(r'seleccionesindicadores', SeleccionIndicadorViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('evaluaciones-indicadores/<int:plataforma_id>/', get_evaluaciones_por_plataforma, name='evaluaciones_por_plataforma'),
]