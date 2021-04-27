from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response

from subscriptions.api.v1.serializers import SubscriptionSerializer

from subscriptions.models import Subscription
from apps.permissions import IsOwner


class SubscriptionViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    """
    list:
        Return a list of all subscriptions.

    create:
        Create a new subscription.

    retrieve:
        Return the given subscription.

    update:
        Update an subscription.

    partial_update:
        Update an subscription.
    """

    serializer_class = SubscriptionSerializer
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = [IsAdminUser | IsOwner]
    http_method_names = ["get", "post", "put", "patch"]

    def get_queryset(self):
        """
        This view should return a list of all subscriptions
        for the currently authenticated user.
        """
        user = self.request.user
        if user.is_anonymous:
            raise PermissionDenied(
                {"detail": "You do not have permission to perform this action."}
            )
        return Subscription.objects.filter(user=user)