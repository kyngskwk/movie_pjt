from django import forms
from .models import Movie, Review, MovieComment, ReviewComment
import requests
import json


class ReviewForm(forms.ModelForm):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content")

    class Meta:
        model = Review
        fields = ['title', 'content', 'movie']


class ReviewForm2(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['title', 'content']


class MovieCommentForm(forms.ModelForm):
    score = forms.IntegerField(
        label='score',
        min_value=0,
        max_value=10,
    )
    content = forms.CharField(label="content")

    # score = forms.IntegerField(widget = forms.Select())

    class Meta:
        model = MovieComment
        fields = ['score', 'content']


class ReviewCommentForm(forms.ModelForm):
    
    content = forms.CharField(label="content")

    class Meta:
        model = ReviewComment
        fields = ['content']