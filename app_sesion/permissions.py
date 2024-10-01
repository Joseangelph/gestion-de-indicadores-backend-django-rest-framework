from rest_framework.permissions import BasePermission

class IsAdministrador(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'administrador'

class IsExperto(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'experto'