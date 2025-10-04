from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView, 
    CommentUpdateView, 
    CommentDeleteView
)

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("register/", views.register_view, name="register"),
    path("profile/", views.profile_view, name="profile"),
    path('posts/', PostListView.as_view(), name='post-list'),         # /posts/
    path('posts/new/', PostCreateView.as_view(), name='post-create'), # /posts/new/
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # /posts/<pk>/
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'), # /posts/<pk>/edit/
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # /posts/<pk>/delete/

    path('post/new/', PostCreateView.as_view(), name='post-create-alias'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update-alias'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete-alias'),
     # Create a new comment on a specific post
    path('posts/<int:post_pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),

    # Edit and delete a comment (identified by comment PK)
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

     path('posts/<int:post_pk>/comments/new/', CommentCreateView.as_view(), name='comment-create-alias'),

    # Edit and delete a comment (identified by comment PK)
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update-alias'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete-alias'),
    ]
