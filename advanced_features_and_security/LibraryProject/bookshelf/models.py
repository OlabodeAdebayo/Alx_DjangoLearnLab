from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    class Meta:
        permissions = [
            ("can_view_book", "Can View Book"),
            ("can_create_book", "Can Create Book"),
            ("can_edit_book", "Can Edit Book"),
            ("can_delete_book", "Can Delete Book"),
        ]

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
