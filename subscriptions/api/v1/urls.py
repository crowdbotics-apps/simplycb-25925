from rest_framework.routers import DefaultRouter

from subscriptions.api.v1.viewsets import SubscriptionViewSet

router = DefaultRouter()

router.register("subscriptions", SubscriptionViewSet, basename="subscriptions")
