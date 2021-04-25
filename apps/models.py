from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


APP_TYPE_CHOICES = [
    ("Web", "Web"),
    ("Mobile", "Mobile"),
]


APP_FRAMEWORK_CHOICES = [
    ("Django", "Django"),
    ("React Native", "React Native"),
]


class App(models.Model):
    name = models.CharField(
        _("Name"),
        max_length=50,
    )
    description = models.TextField(
        _("Description"),
        blank=True,
    )
    type = models.CharField(
        _("Type"),
        max_length=6,
        choices=APP_TYPE_CHOICES,
    )
    framework = models.CharField(
        _("Framework"),
        max_length=12,
        choices=APP_FRAMEWORK_CHOICES,
    )
    domain_name = models.CharField(
        _("Domain name"),
        blank=True,
        max_length=50,
    )
    screenshot = models.ImageField(
        _("Screenshot"),
        blank=True,
        max_length=50,
    )
    # subscription = models.ForeignKey(
    #     "subscriptions.Subscription",
    #     _("Subscription"),
    #     blank=True,
    #     null=True
    # )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
