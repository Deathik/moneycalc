from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission for restricting not owners get detailed data of calculator
    """

    def has_object_permission(self, request, view, obj):
        try:
            return obj.calculator.user == request.user
        except AttributeError:
            return obj.user == request.user
