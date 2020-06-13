from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/movie_list.html', context)


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.review_set.all()
    context = {
        'movie': movie,
        'reviews': reviews
    }
    return render(request, 'movies/movie_detail.html', context)


def review_list(request):
    reviews = Review.objects.all()
    context =  {
        'reviews': reviews
    }
    return render(request, 'movies/review_list.html', context)


def review_create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
            return redirect('movies:movie_detail', review.movie.id)

    else:
        review_form = ReviewForm()

    context = {
        'review_form': review_form,
    }
    return render(request, 'movies/review_create.html', context)


def review_detail(request, movie_id, review_id):
   movie = get_object_or_404(Movie, id=movie_id)
   review = get_object_or_404(Review, id=review_id)
   context = {
       'movie': movie,
       'review': review
   }
   return render(request, 'movies/review_detail.html', context)



    