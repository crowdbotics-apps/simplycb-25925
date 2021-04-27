from django.http import HttpRequest

from rest_framework import serializers

from apps.models import App


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = [
            "id",
            "name",
            "description",
            "type",
            "framework",
            "domain_name",
            "screenshot",
            "subscription",
            "user",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["user", "subscription"]

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
        Override the create function here to associate the created App
        with the User who created it
        """
        app = App.objects.create(**validated_data)
        request = self._get_request()
        app.user = request.user
        app.save()
        return app