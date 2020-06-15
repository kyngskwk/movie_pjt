from django.contrib import admin
from .models import Movie, Review, MovieComment, ReviewComment, Cast

admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(MovieComment)
admin.site.register(ReviewComment)
admin.site.register(Cast)
# Register your models here.
