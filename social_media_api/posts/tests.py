from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()

class PostAPITests(APITestCase):
    def setUp(self):
        # Create two users
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')
        
        # Create a post for user1
        self.post = Post.objects.create(author=self.user1, title="User 1 Post", content="Content")
        
        # URLs
        self.list_url = reverse('post-list') # Matches router name 'post'
        self.detail_url = reverse('post-detail', kwargs={'pk': self.post.pk})

    def test_create_post_authenticated(self):
        """Test that an authenticated user can create a post."""
        self.client.force_authenticate(user=self.user1)
        data = {"title": "New Post", "content": "New Content"}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)

    def test_update_other_user_post_fails(self):
        """Test that user2 cannot update user1's post."""
        self.client.force_authenticate(user=self.user2)
        data = {"title": "Hacked Title"}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_own_post(self):
        """Test that a user can delete their own post."""
        self.client.force_authenticate(user=self.user1)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_search_filter(self):
        """Test the search functionality."""
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(self.list_url, {'search': 'User 1'})
        self.assertEqual(len(response.data['results']), 1)