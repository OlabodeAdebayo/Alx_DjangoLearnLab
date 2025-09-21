from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()       # Use the Book model as the queryset
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()         # Retrieve all Book records
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can access
