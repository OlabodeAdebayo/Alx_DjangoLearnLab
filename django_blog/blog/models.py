from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    #Blog post model representing a single articl.

    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title

     def get_absolute_url(self):
        # Useful for generic CreateView/UpdateView redirecting to detail
        return reverse("post-detail", kwargs={"pk": self.pk})

class Comment(models.Model):
    """
    Comment left by a user on a Post.
    - post: FK to the Post the comment belongs to
    - author: FK to User who wrote the comment
    - content: text of comment
    - created_at: when comment was created
    - updated_at: when comment was last edited
    """
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']  # oldest first; change to '-created_at' for newest first

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
