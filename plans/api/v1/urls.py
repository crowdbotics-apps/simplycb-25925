from rest_framework.routers import DefaultRouter

from plans.api.v1.viewsets import PlanViewSet

router = DefaultRouter()
router.register("plans", PlanViewSet, basename="plans")
