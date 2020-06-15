from django.db import models
from django.conf import settings


# Create your models here.


class Cast(models.Model):
    character = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    poster_path = models.CharField(max_length=200, null=True)
    overview = models.TextField(blank=True)
    gender = models.IntegerField()
    profile_path = models.CharField(max_length=200, null=True)
    imdb_id = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(blank=True)
    poster_path = models.CharField(max_length=200, null=True)
    cast = models.ManyToManyField(Cast, related_name='cast_movie', blank=True)

    def __str__(self):
        return self.title
   
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


class MovieComment(models.Model):
    score = models.IntegerField()
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class ReviewComment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

