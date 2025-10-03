from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("register/", views.register_view, name="register"),
    path("profile/", views.profile_view, name="profile"),
    path('posts/', views.PostListView.as_view(), name='post-list'),         # /posts/
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'), # /posts/new/
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'), # /posts/<pk>/
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'), # /posts/<pk>/edit/
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'), # /posts/<pk>/delete/
    ]
