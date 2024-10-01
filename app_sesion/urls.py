from django.urls import path,include
from .views import CustomTokenObtainPairView, CustomUserViewSet
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import RegisterView

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registrar/', RegisterView.as_view(), name='register'),
]