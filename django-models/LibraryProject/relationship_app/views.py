from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic.detail import DetailView
from .models import Library, Book, UserProfile

# Register View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after registration
            return redirect('list_books')  # redirect to books page or wherever you want
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list_books')  # after login, go to books
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


# Logout View
@login_required
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')
# --- Role checks ---
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# --- Admin View ---
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


# --- Librarian View ---
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


# --- Member View ---
@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    """
    Display details of a specific library, including its books.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
