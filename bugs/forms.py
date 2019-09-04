from django import forms
from .models import Bug, BugComment


class CreateBugForm(forms.ModelForm):
    """Form to create bugs"""
    class Meta:
        model = Bug
        fields = ('name', 'description')


class BugCommentForm(forms.ModelForm):
    """Form to create bug comments"""
    class Meta:
        model = BugComment
        fields = ('comment',)
