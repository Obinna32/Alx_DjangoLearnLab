from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):
    """
    Test suite for Book API endpoints.
    Covers CRUD operations, permissions, filtering, and searching.
    """

    def setUp(self):
        # Create a test user for authenticated endpoints
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        
        # Create an author
        self.author = Author.objects.create(name="Chinua Achebe")
        
        # Create initial books
        self.book1 = Book.objects.create(
            title="Things Fall Apart", 
            publication_year=1958, 
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="Arrow of God", 
            publication_year=1964, 
            author=self.author
        )
        
        # URLs
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        # Details/Update/Delete URLs require pk
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        self.update_url = reverse('book-update', kwargs={'pk': self.book1.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book1.pk})

    # --- Test CRUD Operations ---

    def test_list_books(self):
        """Test retrieving the list of books (Public)."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_book(self):
        """Test retrieving a single book detail (Public)."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book_authenticated(self):
        """Test creating a book as an authenticated user."""
        self.client.login(username='testuser', password='testpassword123')
        data = {
            "title": "No Longer at Ease",
            "publication_year": 1960,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Test that unauthenticated users cannot create books."""
        data = {"title": "Unauthorized", "publication_year": 2000, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        """Test updating a book as an authenticated user."""
        self.client.login(username='testuser', password='testpassword123')
        data = {"title": "Updated Title", "publication_year": 1958, "author": self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        """Test deleting a book as an authenticated user."""
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # --- Test Filtering, Searching, and Ordering ---

    def test_filter_books_by_year(self):
        """Test filtering books by publication year."""
        response = self.client.get(self.list_url, {'publication_year': 1958})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Things Fall Apart")

    def test_search_books_by_title(self):
        """Test searching books by title keyword."""
        response = self.client.get(self.list_url, {'search': 'Arrow'})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Arrow of God")

    def test_ordering_books_by_year(self):
        """Test ordering books by publication year."""
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        # Book1 (1958) should come before Book2 (1964)
        self.assertEqual(response.data[0]['title'], "Things Fall Apart")