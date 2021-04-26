from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from apps.api.v1.serializers import AppSerializer

from apps.models import App
from apps.permissions import IsOwner


class AppViewSet(ModelViewSet):
    """
    list:
        Return a list of all apps.

    create:
        Create a new app.

    retrieve:
        Return the given app.

    update:
        Update an app.

    partial_update:
        Update an app.

    destroy:
        Delete an app.
    """

    serializer_class = AppSerializer
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = [IsAdminUser | IsOwner]
    http_method_names = ["get", "post", "put", "patch", "delete"]

    def get_queryset(self):
        """
        This view should return a list of all apps
        for the currently authenticated user.
        """
        user = self.request.user
        if user.is_anonymous:
            raise PermissionDenied(
                {"detail": "You do not have permission to perform this action."}
            )
        return App.objects.filter(user=user)