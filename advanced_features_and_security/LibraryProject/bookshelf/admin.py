from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser


# Extend UserAdmin to include custom fields for CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")

    fieldsets = (
        (None, {"fields": ("username", "email", "password", "date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "date_of_birth", "profile_photo", "is_staff", "is_active")}
        ),
    )

    search_fields = ("username", "email")
    ordering = ("username",)
    
    
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
