from django.http import HttpRequest

from rest_framework import serializers

from subscriptions.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
        read_only_fields = ["user"]

    def _get_request(self):
        request = self.context.get("request")
        if (
            request
            and not isinstance(request, HttpRequest)
            and hasattr(request, "_request")
        ):
            request = request._request
        return request

    def create(self, validated_data):
        """
        Override the create function here to associate the created Subscription
        with the User who created it
        """
        subscription = Subscription.objects.create(**validated_data)
        request = self._get_request()
        subscription.user = request.user
        subscription.save()
        return subscription