from django.db import models
from django.conf import settings

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(blank=True)
    vote_average = models.IntegerField()
    poster_path = models.CharField(max_length=200, null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)

   
   
    # adult = models.BooleanField(blank=True)
    # original_title = models.CharField(max_length=255, blank=True)
    # video = models.BooleanField(blank=True) 
    # vote_count = models.IntegerField(blank=True)
    # overview = models.CharField(max_length=255, blank=True)
    # genre_ids = models.CharField(max_length=255, blank=True)
    

class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)