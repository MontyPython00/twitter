from django import forms
from posts.models import Post, Comment, Like
from django.contrib.auth import get_user

class PostCreateForm(forms.ModelForm):
    description = forms.CharField(label='Content', widget=forms.Textarea(attrs={'placeholder': 'Write here...'}))
    class Meta:
        model = Post
        fields = ['description']


class CommentCreateForm(forms.ModelForm):
    text = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'Write comment here...',
                                                                  'class': 'post-detail-add-comment-textarea'}))

    class Meta:
        model = Comment
        fields = ['text']


class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = []
