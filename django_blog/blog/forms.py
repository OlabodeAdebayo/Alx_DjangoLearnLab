from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PostForm(forms.ModelForm):
    """
    Form for creating/updating Post.
    The author is set in the view from request.user; not provided by the form.
    """
    class Meta:
        model = Post
        fields = ['title', 'content']  # author & published_date handled automatically
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post title', 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your post...', 'class': 'form-control', 'rows': 10}),
        }

class CommentForm(forms.ModelForm):
    """
    ModelForm for comments. Validates that content is not empty or only whitespace.
    """
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write your comment here...'
            })
        }

    def clean_content(self):
        data = self.cleaned_data.get('content', '')
        if not data or not data.strip():
            raise forms.ValidationError("Comment cannot be empty.")
        return data.strip()
