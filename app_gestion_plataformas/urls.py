from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (PlataformasTecnologicasViewSet)

router = DefaultRouter()
router.register('plataformas', PlataformasTecnologicasViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]