from django.contrib import admin
from .models import Movie, Review, MovieComment, ReviewComment

admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(MovieComment)
admin.site.register(ReviewComment)


# Register your models here.
