from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class Subscription(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    plan = models.ForeignKey(
        "plans.Plan",
        on_delete=models.CASCADE,
    )
    app = models.OneToOneField(
        "apps.App",
        on_delete=models.CASCADE,
    )
    active = models.BooleanField(
        _("Active"),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Subscription #{self.id} for {self.user}"