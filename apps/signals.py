from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.models import App
from plans.models import Plan
from subscriptions.models import Subscription


@receiver(post_save, sender=App)
def create_subscription(sender, instance, **kwargs):
    # Only create subscription if app is associated with user and does not have
    # a subscription
    if instance.user and not hasattr(instance, "subscription"):
        Subscription.objects.create(
            user=instance.user,
            plan=Plan.objects.get(name="Free"),
            app=instance,
            active=True,
        )
