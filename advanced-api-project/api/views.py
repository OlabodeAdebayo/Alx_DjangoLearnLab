from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer


# ListView – Retrieve all books
class BookListView(generics.ListAPIView):
    """
    Returns a list of all books.
    Read-only, available to everyone.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# DetailView – Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    Returns details of a specific book.
    Read-only, available to everyone.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# CreateView – Add a new book
class BookCreateView(generics.CreateAPIView):
    """
    Allows authenticated users to create a new book.
    Custom validation is already handled in BookSerializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Hook for extra logic after validation but before saving.
        Example: attach metadata, log events, or enforce extra rules.
        """
        # Example of custom behavior:
        # Ensure title is capitalized before saving
        title = serializer.validated_data.get('title', '').title()
        serializer.save(title=title)


# UpdateView – Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    Allows authenticated users to update an existing book.
    Only PUT/PATCH requests.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Additional customization before saving updates.
        """
        # Example: trim whitespace around title
        title = serializer.validated_data.get('title', '').strip()
        serializer.save(title=title)


# DeleteView – Remove a book
class BookDeleteView(generics.DestroyAPIView):
    """
    Allows authenticated users to delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookListCreateView(generics.ListCreateAPIView):
    """
    List all books or create a new one.
    Supports:
      - Filtering by title, author__name, publication_year
      - Searching by title and author name
      - Ordering by title or publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Add DRF filter backends
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Filtering options
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Search options (partial matches)
    search_fields = ['title', 'author__name']

    # Ordering options
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering
