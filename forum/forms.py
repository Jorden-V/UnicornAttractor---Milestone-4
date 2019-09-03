from django import forms
from .models import ForumPost, ForumComment


class ForumPostForm(forms.ModelForm):
    """Form ti create forum posts"""
    class Meta:
        model = ForumPost
        fields = ('name', 'description')


class ForumCommentForm(forms.ModelForm):
    """form to create forum post comments"""
    class Meta:
        model = ForumComment
        fields = ('comment',)
