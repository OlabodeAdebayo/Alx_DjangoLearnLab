from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints.
    Covers CRUD, filtering, searching, ordering, and permissions.
    """

    def setUp(self):
        # Create a test user for authenticated endpoints
        self.user = User.objects.create_user(
            username='testuser', password='testpass123'
        )

        # Create sample authors and books
        self.author1 = Author.objects.create(name='Author One')
        self.author2 = Author.objects.create(name='Author Two')

        self.book1 = Book.objects.create(
            title='Python Basics',
            publication_year=2022,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title='Django Advanced',
            publication_year=2023,
            author=self.author2
        )

        # Endpoint URLs
        self.list_url = reverse('book-list')  # /api/books/
        self.detail_url = reverse('book-detail', args=[self.book1.id])

    # ---------- CRUD TESTS ----------

    def test_list_books(self):
        """Anyone should be able to list all books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_requires_authentication(self):
        """Unauthenticated users should NOT be able to create books."""
        data = {
            'title': 'New Book',
            'publication_year': 2024,
            'author': self.author1.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        """Authenticated users can create a new book."""
        self.client.login(username='testuser', password='testpass123')
        data = {
            'title': 'New Book',
            'publication_year': 2024,
            'author': self.author1.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, 'New Book')

    def test_retrieve_book_detail(self):
        """Anyone can retrieve details of a specific book."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Python Basics')

    def test_update_book_authenticated(self):
        """Authenticated users can update a book."""
        self.client.login(username='testuser', password='testpass123')
        data = {'title': 'Python Basics Updated', 'publication_year': 2022, 'author': self.author1.id}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Python Basics Updated')

    def test_delete_book_authenticated(self):
        """Authenticated users can delete a book."""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    # ---------- FILTERING / SEARCH / ORDERING ----------

    def test_filter_books_by_author(self):
        """Filter by author's name."""
        response = self.client.get(f"{self.list_url}?author__name=Author One")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Python Basics')

    def test_search_books_by_title(self):
        """Search for books containing 'Django'."""
        response = self.client.get(f"{self.list_url}?search=Django")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Django Advanced')

    def test_order_books_by_publication_year_desc(self):
        """Order books by publication_year descending."""
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))

