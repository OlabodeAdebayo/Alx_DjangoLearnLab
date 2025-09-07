from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book, Library

def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    """
    Display details of a specific library, including its books.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
