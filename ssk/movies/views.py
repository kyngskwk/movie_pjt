import requests
import json
from django.http import JsonResponse
from django.db.models import Avg
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .models import Movie, Review, MovieComment, ReviewComment
from .forms import ReviewForm, ReviewForm2, MovieCommentForm, ReviewCommentForm
# Create your views here.


def start(request):
    return render(request, 'movies/start.html')


def movie_list(request):
    movies = Movie.objects.all()
    if request.user.is_authenticated:
        if request.user.moviecomment_set.count() != 0:
            cast_list = request.user.moviecomment_set.order_by('-score')[0].movie.cast.all()
            actor = cast_list[0]
            others = cast_list[1:3]
            inputvalue = actor.title + 'trailer'
        else:
            movie = Movie.objects.order_by('-moviecomment')[0]
            inputvalue = movie.title + 'trailer'

    else:
        movie = Movie.objects.order_by('-moviecomment')[0]
        inputvalue = movie.title + 'trailer'

    url = 'https://www.googleapis.com/youtube/v3/search'

    params = {
        'key': 'AIzaSyDTbIcGHsuUUIRshQMA8M9xBXKzMpIKHK8',
        'part': 'snippet',
        'type': 'video',
        'maxResults': '1',
        'q': inputvalue,
    }

    response = requests.get(url, params)
    response_dict = response.json()

    paginator = Paginator(movies, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'movies': movies,
        'page_obj': page_obj,
        'youtube_items': response_dict['items']
    }
    return render(request, 'movies/movie_list.html', context)


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.review_set.all()
    comments = movie.moviecomment_set.all()
    comments_count = movie.moviecomment_set.count()
    if comments_count != 0:
        score = movie.moviecomment_set.all().aggregate(Avg('score'))
        averages = score['score__avg']
        average = int(averages)

        # average = 
        comment_form = MovieCommentForm()
        context = {
            'comments_count': comments_count,
            'movie': movie,
            'reviews': reviews,
            'comments': comments,
            'comment_form': comment_form,
            'average': average
        }

    else:
        comment_form = MovieCommentForm()
        context = {
            'comments_count': comments_count,
            'movie': movie,
            'reviews': reviews,
            'comments': comments,
            'comment_form': comment_form,
        }
    return render(request, 'movies/movie_detail.html', context)


def review_list(request):
    reviews = Review.objects.all()
    context =  {
        'reviews': reviews
    }
    return render(request, 'movies/review_list.html', context)


@login_required
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
    comments = review.reviewcomment_set.all()
    comment_form = ReviewCommentForm()
    context = {
        'movie': movie,
        'review': review,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'movies/review_detail.html', context)


@login_required
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


@login_required
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
                return redirect('movies:review_detail', review.movie.id, review.id)
            
        else:
            review_form = ReviewForm(instance=review)

        context = {
            'review_form': review_form,
            'review': review,
            'movie': movie
        }
        return render(request, 'movies/review_create.html', context)


@login_required
@require_POST
def review_delete(request, movie_id, review_id):
    movie = get_object_or_404(Movie, id=movie_id)
    review = get_object_or_404(Review, id=review_id)
    if request.user == review.user:
        review.delete()
    return redirect('movies:review_list')


@login_required
def moive_comment_create(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        comment_form = MovieCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.movie = movie
            comment.save()
    return redirect('movies:movie_detail', movie.id)


@require_POST
@login_required
def movie_comment_delete(request, movie_id, comment_id):
    comment = get_object_or_404(MovieComment, id=comment_id)
    if comment.user != request.user:
        return redirect('movies:movie_detail', movie_id)
    comment.delete()
    return redirect('movies:movie_detail', movie_id)


@login_required
def movie_comment_update(request, movie_id, comment_id):
    comment = get_object_or_404(MovieComment, id=comment_id)
    if comment.user == request.user:
        if request.method == 'POST':
            comment_form = MovieCommentForm(request.POST, instance=comment)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('movies:movie_detail', comment.movie.id)

        else:
            comment_form = MovieCommentForm(instance=comment)
        context = {
            'comment_form': comment_form,
        }
        return render(request, 'movies/movie_comment_update.html', context)


@login_required
def review_comment_create(request, movie_id, review_id):
    movie = get_object_or_404(Movie, id=movie_id)
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'POST':
        comment_form = ReviewCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.review = review
            comment.save()
    return redirect('movies:review_detail', movie.id, review_id)


@require_POST
@login_required
def review_comment_delete(request, movie_id, review_id, comment_id):
    comment = get_object_or_404(ReviewComment, id=comment_id)
    if comment.user != request.user:
        return redirect('movies:review_detail', movie_id, review_id)
    comment.delete()
    return redirect('movies:review_detail', movie_id, review_id)





@login_required
def like(request, movie_id, review_id):
    user = request.user
    movie = get_object_or_404(Movie, id=movie_id)
    review = get_object_or_404(Review, id=review_id)

    if review.like_users.filter(id=user.id).exists():
        review.like_users.remove(user)
        liked = False

    else:
        review.like_users.add(user)
        liked = True

    context = {
        'count': review.like_users.count(),
        'liked': liked,
    }

    return JsonResponse(context)
