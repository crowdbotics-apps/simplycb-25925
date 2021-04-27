from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from plans.api.v1.serializers import PlanSerializer
from plans.models import Plan


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
    permission_classes = [IsAuthenticated]
    http_method_names = ["get"]