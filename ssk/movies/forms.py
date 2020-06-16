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
    PICKS = [
        (0, '0점'),
        (1, '1점'),
        (2, '2점'),
        (3, '3점'),
        (4, '4점'),
        (5, '5점'),
        (6, '6점'),
        (7, '7점'),
        (8, '8점'),
        (9, '9점'),
        (10, '10점'),
    ]
    score = forms.ChoiceField(choices=PICKS, widget=forms.Select(), label="별점")
    content = forms.CharField(label="댓글 내용")

    # score = forms.IntegerField(widget = forms.Select())

    class Meta:
        model = MovieComment
        fields = ['score', 'content']


class ReviewCommentForm(forms.ModelForm):
    
    content = forms.CharField(label="댓글 내용")

    class Meta:
        model = ReviewComment
        fields = ['content']