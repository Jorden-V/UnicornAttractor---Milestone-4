from django import forms
from .models import Feature, FeatureComment


class CreateFeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ('name', 'desc')


class FeatureCommentForm(forms.ModelForm):
    class Meta:
        model = FeatureComment
        fields = ('description',)
