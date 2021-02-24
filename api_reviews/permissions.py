from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or request.user.is_staff:
            return True


class IsOwnerOrReadOnlyPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True

        if request.method in SAFE_METHODS:
            return True

        if request.user.is_moderator:
            return True

        return False
