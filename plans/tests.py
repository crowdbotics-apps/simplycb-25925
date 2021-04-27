from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from plans.models import Plan

User = get_user_model()


class PlanTests(APITestCase):
    def setUp(self):
        test_user = User.objects.create_user(username="test_user", password="test1234")
        token = Token.objects.create(user=test_user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        self.free_plan = Plan.objects.create(
            name="Free", description="Free Plan Description", price=0.00
        )
        self.standard_plan = Plan.objects.create(
            name="Standard", description="Standard Plan Description", price=10.00
        )
        self.pro_plan = Plan.objects.create(
            name="Pro", description="Pro Plan Description", price=25.00
        )

    def test_list_plans(self):
        """
        Ensure we can list plans.
        """
        url = reverse("plans-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_plan(self):
        """
        Ensure we can fetch an plan object.
        """
        url = reverse("plans-detail", kwargs={"pk": self.free_plan.id})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.free_plan.id)
        self.assertEqual(response.data["name"], self.free_plan.name)
        self.assertEqual(float(response.data["price"]), self.free_plan.price)

        url = reverse("plans-detail", kwargs={"pk": self.standard_plan.id})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.standard_plan.id)
        self.assertEqual(response.data["name"], self.standard_plan.name)
        self.assertEqual(float(response.data["price"]), self.standard_plan.price)

        url = reverse("plans-detail", kwargs={"pk": self.pro_plan.id})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.pro_plan.id)
        self.assertEqual(response.data["name"], self.pro_plan.name)
        self.assertEqual(float(response.data["price"]), self.pro_plan.price)
