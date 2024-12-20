# permissions.py
from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
   
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'administrador'


class IsAdminOrExpertUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['administrador', 'experto']