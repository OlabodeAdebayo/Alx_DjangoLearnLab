from django.contrib import admin
from .models import Book

# Customize how Book is displayed in the admin

@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    # Columns to display in the list view
    list_display = ("title", "author", "publication_year")
    
    # Add filters (right-hand sidebar in admin)
    list_filter = ("publication_year", "author")
    
    # Enable search functionality
    search_fields = ("title", "author")
