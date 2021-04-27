from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from apps.models import App
from plans.models import Plan

User = get_user_model()


class AppTests(APITestCase):
    def setUp(self):
        test_user = User.objects.create_user(username="test_user", password="test1234")
        token = Token.objects.create(user=test_user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        Plan.objects.create(
            name="Free", description="Free Plan Description", price=0.00
        )
        self.test_app = App.objects.create(
            name="Test App",
            description="Test App Description",
            type="Web",
            framework="Django",
            domain_name="test-app.com",
            user=test_user,
        )

    def test_list_apps(self):
        """
        Ensure we can list apps.
        """
        url = reverse("apps-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_app(self):
        """
        Ensure we can create a new app object.
        """
        url = reverse("apps-list")
        data = {
            "name": "Test Create App",
            "description": "Test Create App Description",
            "type": "Web",
            "framework": "Django",
            "domain_name": "test-create-app.com",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(App.objects.count(), 2)
        self.assertEqual(App.objects.get(id=2).name, "Test Create App")

    def test_retrieve_app(self):
        """
        Ensure we can fetch an app object.
        """
        url = reverse("apps-detail", kwargs={"pk": self.test_app.id})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.test_app.id)

    def test_update_app(self):
        """
        Ensure we can update an app object.
        """
        url = reverse("apps-detail", kwargs={"pk": self.test_app.id})
        data = {
            "name": "Test App PUT",
            "type": "Mobile",
            "framework": "React Native",
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.test_app.id)
        self.assertEqual(response.data["name"], data["name"])
        self.assertEqual(response.data["type"], data["type"])
        self.assertEqual(response.data["framework"], data["framework"])

    def test_partial_update_app(self):
        """
        Ensure we can partial update an app object.
        """
        url = reverse("apps-detail", kwargs={"pk": self.test_app.id})
        data = {
            "name": "Test App PATCH",
        }
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.test_app.id)
        self.assertEqual(response.data["name"], data["name"])

    def test_delete_app(self):
        """
        Ensure we can delete an app object.
        """
        url = reverse("apps-detail", kwargs={"pk": self.test_app.id})
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
