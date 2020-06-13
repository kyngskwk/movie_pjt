from django.urls import path
from . import views


app_name = 'movies'


urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('review_list/', views.review_list, name='review_list'),
    path('review_create/', views.review_create, name='review_create'),
    path('<int:movie_id>/<int:review_id>/', views.review_detail, name='review_detail'),
]