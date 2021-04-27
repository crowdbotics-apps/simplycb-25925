from django.contrib import admin

from apps.models import App


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    # Returning a URL to the actual subscription might be a good idea here!
    def get_subscription_id(self, obj):
        return obj.subscription.id

    get_subscription_id.short_description = "Subscription ID"

    readonly_fields = ["get_subscription_id"]