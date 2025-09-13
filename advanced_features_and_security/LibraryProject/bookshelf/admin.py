from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser


# Extend UserAdmin to include custom fields for CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active", "date_of_birth")
    search_fields = ("username", "email")

    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )


# Register CustomUser
admin.site.register(CustomUser, CustomUserAdmin)


# Keep your existing Book admin
@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    # Columns to display in the list view
    list_display = ("title", "author", "publication_year")
    
    # Add filters (right-hand sidebar in admin)
    list_filter = ("publication_year", "author")
    
    # Enable search functionality
    search_fields = ("title", "author")
