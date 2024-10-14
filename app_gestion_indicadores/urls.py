from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (IndicadorViewSet
                    ,CategoriaAnalisisViewSet, DestinoImpactoViewSet, ComponenteViewSet, DimensionViewSet,
                    SubdimensionViewSet)
from .views import toggle_habilitado

router = DefaultRouter()
router.register('categorias', CategoriaAnalisisViewSet)
router.register('destinos', DestinoImpactoViewSet)
router.register('componentes', ComponenteViewSet)
router.register('dimensiones', DimensionViewSet)
router.register('subdimensiones', SubdimensionViewSet)
router.register('indicadores', IndicadorViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('<str:model_name>/<int:pk>/toggle-habilitado/', toggle_habilitado, name='toggle-habilitado'),
]