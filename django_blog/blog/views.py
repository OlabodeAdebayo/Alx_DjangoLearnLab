from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

# --- Extend UserCreationForm for Registration ---
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# --- Register View ---
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = CustomUserCreationForm()
    return render(request, "auth/register.html", {"form": form})

# --- Login View ---
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
    else:
        form = AuthenticationForm()
    return render(request, "auth/login.html", {"form": form})

# --- Logout View ---
def logout_view(request):
    logout(request)
    return redirect("login")

# --- Profile View ---
@login_required
def profile_view(request):
    if request.method == "POST":
        request.user.email = request.POST.get("email", request.user.email)
        request.user.save()
        return redirect("profile")
    return render(request, "auth/profile.html", {"user": request.user})

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"  # override default template name
    context_object_name = "posts"
    ordering = ['-published_date']  # newest first
    paginate_by = 10  # optional

# Show a single post
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

# Create new post - only logged-in users
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    # form_valid sets the author automatically
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update a post - only the author can update
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        # Ensure the author is not changed
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        # Only author can edit
        return self.request.user == post.author

# Delete a post - only the author can delete
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
