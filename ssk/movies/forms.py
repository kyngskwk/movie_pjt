from django import forms
from .models import Movie, Review, MovieComment, ReviewComment
import requests
import json


class ReviewForm(forms.ModelForm):
    

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

    # score = forms.IntegerField(widget = forms.Select())

    class Meta:
        model = MovieComment
        fields = ['score', 'content']


class ReviewCommentForm(forms.ModelForm):
    

    class Meta:
        model = ReviewComment
        fields = ['content']