from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm
from movies.models import Movie, Cast




User = get_user_model()

# Create your views here.



def signup(request):
    # 로그인 되어있다면
    if request.user.is_authenticated:
        return redirect('movies:movie_list')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:movie_list')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('movies:movie_list')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'movies:movie_list')

    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:movie_list')
    

@login_required
def profile(request, username):
    User = get_user_model()
    person = get_object_or_404(User, username=username)
    if person.moviecomment_set.count() != 0:
        cast_list = person.moviecomment_set.order_by('-score')[0].movie.cast.all()
        # movies = person.moviecomment_set.order_by('-score').values('movie_id')
        # casts = Movie.objects.filter(movie_id=movies).cast_id
    else:
        cast_list = Movie.objects.order_by('-moviecomment')[0].movie.cast.all()
 
    context = {
        'person': person,
        # 'movies': movies,
        'cast_list': cast_list,
  
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def follow(request, username):
    me = request.user
    you = get_object_or_404(get_user_model(), username=username)

    if me != you:
        if you.followers.filter(id=me.id).exists():
            you.followers.remove(me)
        else:
            you.followers.add(me)
    return redirect('accounts:profile', username)