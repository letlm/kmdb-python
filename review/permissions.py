from rest_framework import permissions
from rest_framework.views import Request, View


class IsCriticOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj):
        if request.user.is_staff:
            return True

        if not request.user.is_critic:
            return False

        if request.user.id == obj.id:
            return True
