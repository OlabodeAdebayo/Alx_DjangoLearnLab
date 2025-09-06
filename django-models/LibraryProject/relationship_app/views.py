from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library, Book


def list_books(request):
    # Retrieves all books and renders a template displaying the list.
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(Detailview):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context
