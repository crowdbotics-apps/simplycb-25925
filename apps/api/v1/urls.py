from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.api.v1.viewsets import AppViewSet

router = DefaultRouter()
router.register("apps", AppViewSet)
