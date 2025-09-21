from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()       # Use the Book model as the queryset
    serializer_class = BookSerializer
# Create your views here.
