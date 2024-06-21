# -*- coding: utf-8 -*-
from django import forms
from .models import ArticleImage, Feedback


class ArticleImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'allow_multiple_selected': True}))


class Meta:
    model = ArticleImage
    fields = '__all__'


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'feedback']