from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (IndicadorViewSet
                    ,CategoriaAnalisisViewSet, DestinoImpactoViewSet, ComponenteViewSet, DimensionViewSet,
                    SubdimensionViewSet)

router = DefaultRouter()
router.register('categorias', CategoriaAnalisisViewSet)
router.register('destinos', DestinoImpactoViewSet)
router.register('componentes', ComponenteViewSet)
router.register('dimensiones', DimensionViewSet)
router.register('subdimensiones', SubdimensionViewSet)
router.register('indicadores', IndicadorViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]