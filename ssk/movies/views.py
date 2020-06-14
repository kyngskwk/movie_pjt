from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review
from .forms import ReviewForm, ReviewForm2
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
            # review.movie = movie
            review.save()
            return redirect('movies:review_detail', review.movie.id, review.id)

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



def review_c(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        review_form = ReviewForm2(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
            return redirect('movies:review_detail', review.movie.id, review.id)

    else:
        review_form = ReviewForm2()

    context = {
        'movie': movie,
        'review_form': review_form,
    }
    return render(request, 'movies/movie_review.html', context)


def review_update(request, movie_id, review_id):
    movie = get_object_or_404(Movie, id=movie_id)
    review = get_object_or_404(Review, id=review_id)
    if request.user == review.user:
        if request.method == 'POST':
            review_form = ReviewForm(request.POST, instance=review)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.user = request.user
                review.save()
                return redirect('movies:review_detail', review.movie.pk, review.id)
            
        else:
            review_form = ReviewForm(instance=review)

        context = {
            'review_form': review_form,
            'review': review,
            'movie': movie
        }
        return render(request, 'movies/review_create.html', context)

