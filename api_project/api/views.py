from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()       # Use the Book model as the queryset
    serializer_class = BookSerializer
# Create your views here.
