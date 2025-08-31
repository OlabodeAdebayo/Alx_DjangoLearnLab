# CRUD Operations for Book Model

# Create
```python
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Expected output: <Book: 1984 by George Orwell (1949)>

book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
# Expected output: ('1984', 'George Orwell', 1949)

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book
# Expected output: <Book: Nineteen Eighty-Four by George Orwell (1949)>

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Expected output: (1, {'bookshelf.Book': 1})

Book.objects.all()
# Expected output: <QuerySet []>
