from django.db import models
from django.utils.translation import ugettext_lazy as _


class Plan(models.Model):
    """
    This model represents a Plan instance.
    """

    name = models.CharField(
        _("Name"),
        max_length=20,
    )
    description = models.TextField(
        _("Description"),
    )
    price = models.DecimalField(
        _("Price"),
        max_digits=4,
        decimal_places=2,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ${self.price}"