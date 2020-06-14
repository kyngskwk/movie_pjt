from django import forms
from .models import Movie, Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['title', 'content', 'movie']
        

class ReviewForm2(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['title', 'content']