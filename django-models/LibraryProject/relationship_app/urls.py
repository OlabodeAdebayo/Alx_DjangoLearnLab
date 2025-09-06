from django.urls import path
from .views import list_books

urlpatterns = [
        path('books/', list_books, name='list_books'),
        path('library/<int:pk>/', views.`:wqLibraryDetailView.as_view(), name='library_detail')
