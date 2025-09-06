from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library


def list_books(request):
    # Retrieves all books and renders a template displaying the list.
    books = Book.objects.all()
    response_text = "\n".join([f"{book.title} by {book.author.name}" for book in books])


    return HttpResponse(response_text, content_type="text/plain")

class LibraryDetailView(Detailview):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.objects.books.all()
        return context
