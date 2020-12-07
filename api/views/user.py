from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from ..serializers import UserSerializer


class ProfilePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (ProfilePermission,)
