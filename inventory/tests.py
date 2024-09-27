from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Item


class APITest(APITestCase):

    def setUp(self):
        # Create a user to authenticate
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")
        # Create an item for testing
        self.item = Item.objects.create(name="Test Item", description="Test description")

    def test_user_registration(self):
        """Test that a user can register successfully"""
        url = reverse("user-register")
        data = {"username": "newuser", "password": "newpassword123"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["status"], "User created")

    def test_user_registration_existing_user(self):
        """Test that registration fails if the username already exists"""
        url = reverse("user-register")
        data = {"username": "testuser", "password": "password123"}  # Already existing username
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["error"], "Username already exists.")

    def test_create_item(self):
        """Test creating an item"""
        url = reverse("create_item")
        data = {"name": "New Item", "description": "New item description"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "New Item")

    def test_get_item(self):
        """Test retrieving an item"""
        url = reverse("item_detail", kwargs={"pk": self.item.pk})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.item.name)

    def test_update_item(self):
        """Test updating an item"""
        url = reverse("item_detail", kwargs={"pk": self.item.pk})
        data = {"name": "Updated Item", "description": "Updated description"}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated Item")

    def test_delete_item(self):
        """Test deleting an item"""
        url = reverse("item_detail", kwargs={"pk": self.item.pk})
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

