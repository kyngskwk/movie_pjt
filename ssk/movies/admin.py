from django.contrib import admin
from .models import Movie, Review, MovieComment

admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(MovieComment)

# Register your models here.
