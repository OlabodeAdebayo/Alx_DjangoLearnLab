from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Tag
from taggit.forms import TagWidget

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Enter tags separated by commas")

    """
    Form for creating/updating Post.
    The author is set in the view from request.user; not provided by the form.
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # author & published_date handled automatically
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post title', 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your post...', 'class': 'form-control', 'rows': 10}),
            'tags': TagWidget(),
        }
    
        def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        # handle tags manually
        tags_str = self.cleaned_data.get("tags", "")
        if tags_str:
            tags_list = [t.strip() for t in tags_str.split(",")]
            for tag_name in tags_list:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                instance.tags.add(tag)
        return instance

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
