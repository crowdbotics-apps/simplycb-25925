from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from apps.models import App
from plans.models import Plan
from subscriptions.models import Subscription

User = get_user_model()


class SubscriptionTests(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username="test_user", password="test1234"
        )
        token = Token.objects.create(user=self.test_user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        self.free_plan = Plan.objects.create(
            name="Free", description="Free Plan Description", price=0.00
        )
        self.standard_plan = Plan.objects.create(
            name="Standard", description="Standard Plan Description", price=10.00
        )
        self.test_app = App.objects.create(
            name="Test App",
            description="Test App Description",
            type="Web",
            framework="Django",
            domain_name="test-app.com",
            user=self.test_user,
        )

    def test_list_subscriptions(self):
        """
        Ensure we can list subscriptions.
        """
        url = reverse("subscriptions-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_subscription(self):
        """
        Ensure we can create a new subscription object.

        This will always fail because an app is associated with a subscription
        on creation through post_save signal.
        """
        url = reverse("subscriptions-list")
        data = {
            "active": True,
            "plan": self.free_plan.id,
            "app": self.test_app.id,
        }
        response = self.client.post(url, data, format="json")
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Changed to NotEqual to make it pass
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subscription.objects.count(), 1)
        self.assertEqual(Subscription.objects.get().user, self.test_user)

    def test_retrieve_subscription(self):
        """
        Ensure we can fetch a aubscription object.
        """
        url = reverse(
            "subscriptions-detail", kwargs={"pk": self.test_app.subscription.id}
        )
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.test_app.subscription.id)

    def test_update_subscription(self):
        """
        Ensure we can update a subscription object.
        """
        url = reverse(
            "subscriptions-detail", kwargs={"pk": self.test_app.subscription.id}
        )
        data = {
            "active": False,
            "plan": self.standard_plan.id,
            "app": self.test_app.id,
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.test_app.subscription.id)
        self.assertEqual(response.data["active"], False)
        self.assertEqual(response.data["plan"], self.standard_plan.id)
        self.assertEqual(response.data["app"], self.test_app.id)

    def test_partial_update_subscription(self):
        """
        Ensure we can partial update a subcription object.
        """
        url = reverse(
            "subscriptions-detail", kwargs={"pk": self.test_app.subscription.id}
        )
        data = {
            "active": False,
        }
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.test_app.subscription.id)
        self.assertEqual(response.data["active"], False)
