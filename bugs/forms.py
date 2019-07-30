from django import forms
from .models import Bug, BugComment

class CreateBugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('name', 'desc')
        
class BugCommentForm(forms.ModelForm):
    class Meta:
        model = BugComment
        fields=('description',)