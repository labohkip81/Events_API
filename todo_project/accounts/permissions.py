from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerProfileReadOnly(BasePermission):
    def has_object_permission(self, obj, request, view):
        if request.method in SAFE_METHODS:
            return True

        return obj.user==request.user