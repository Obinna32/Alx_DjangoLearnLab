from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class FollowTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')
        self.client.force_authenticate(user=self.user1)

    def test_follow_user(self):
        url = reverse('follow-user', kwargs={'user_id': self.user2.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.user1.following.filter(id=self.user2.id).exists())

    def test_unfollow_user(self):
        self.user1.following.add(self.user2)
        url = reverse('unfollow-user', kwargs={'user_id': self.user2.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(self.user1.following.filter(id=self.user2.id).exists())