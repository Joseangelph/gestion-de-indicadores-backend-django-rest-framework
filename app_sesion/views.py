from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework import generics
from .models import CustomUser
from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer, UserSerializer
from rest_framework import viewsets

from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [AllowAny]
    
    
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]  # Permite que cualquier usuario acceda a esta vista
    
    

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]