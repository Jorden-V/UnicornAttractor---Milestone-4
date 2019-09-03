from django import forms
from .models import Feature, FeatureComment


class CreateFeatureForm(forms.ModelForm):
    """Form to create feature requests"""
    class Meta:
        model = Feature
        fields = ('name', 'description')


class FeatureCommentForm(forms.ModelForm):
    """Form to create feature comments"""
    class Meta:
        model = FeatureComment
        fields = ('comment',)
