from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.models import App
from plans.models import Plan
from subscriptions.models import Subscription

free_plan, _ = Plan.objects.get_or_create(
    name="Free", description="Free Plan Description", price="0.00"
)


@receiver(post_save, sender=App)
def create_subscription(sender, instance, **kwargs):
    # Only create subscription if app is associated with user and does not have
    # a subscription
    if instance.user and not hasattr(instance, "subscription"):
        Subscription.objects.create(
            user=instance.user,
            plan=free_plan,
            app=instance,
            active=True,
        )
