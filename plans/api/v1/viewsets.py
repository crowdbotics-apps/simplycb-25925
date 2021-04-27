from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response

from plans.api.v1.serializers import PlanSerializer
from plans.models import Plan

from apps.permissions import IsOwner


class PlanViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    """
    list:
        Return a list of all plans.

    retrieve:
        Return the given plan.
    """

    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = [IsAdminUser | IsOwner]
    http_method_names = ["get"]