from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone


class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book fields.
    Adds validation to prevent future publication years.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author and nests all related books.
    Uses BookSerializer (many=True) to include related Book objects.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
