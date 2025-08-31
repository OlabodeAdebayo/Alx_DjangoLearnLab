# Delete Operation

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Expected output: (1, {'bookshelf.Book': 1})

Book.objects.all()

# Expected output: <QuerySet []>
