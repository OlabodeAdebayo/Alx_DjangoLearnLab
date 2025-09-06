import os
import django

# Configure Django settings for standalone script
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def sample_data():
    # Create author and books
    jane = Author.objects.create(name='Jane Austen')
    pride = Book.objects.create(title='Pride and Prejudice', author=jane)
    emma = Book.objects.create(title='Emma', author=jane)

    # Create library and assign books
    central = Library.objects.create(name='Central Library')
    central.books.set([pride, emma])

    # Create librarian for that library
    Librarian.objects.create(name='Alice', library=central)

    return jane, central

def query_all_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return author.books.all()

def query_all_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def query_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

if __name__ == '__main__':
    jane, central = sample_data()

    print("Books by Jane Austen:")
    for book in query_all_books_by_author('Jane Austen'):
        print('-', book.title)

    print("\nBooks in Central Library:")
    for book in query_all_books_in_library('Central Library'):
        print('-', book.title)

    print("\nLibrarian at Central Library:")
    print('-', query_librarian_for_library('Central Library').name)

