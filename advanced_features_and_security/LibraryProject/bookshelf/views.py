from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookSearchForm
from django.utils.decorators import decorator_from_middleware
from django.views.decorators.clickjacking import xframe_options_sameorigin

def add_csp_header(get_response):
    def middleware(request):
        response = get_response(request)
        response['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; style-src 'self' https://fonts.googleapis.com"
        return response
    return middleware

def search_books(request):
    form = BookSearchForm(request.GET or None)
    results = []

    if form.is_valid():
        query = form.cleaned_data.get("q")
        results = Book.objects.filter(title__icontains=query)

    return render(request, "bookshelf/search_results.html", {"form": form, "results": results})

@permission_required('bookshelf.can_view', raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    # logic for adding a book
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # logic for editing
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')
