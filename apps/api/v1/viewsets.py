from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from apps.api.v1.serializers import AppSerializer

from apps.models import App


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
    queryset = App.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = [IsAdminUser]
    http_method_names = ["get", "post", "put", "patch", "delete"]