from django.urls import path
from . import views


app_name = 'movies'


urlpatterns = [
    path('', views.start, name='start'),
    # 영화 리스트
    path('index/', views.movie_list, name='movie_list'),
    # 영화 디테일
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_id>/review_create/', views.review_c, name='review_c' ),
    path('<int:movie_id>/movie_comments/', views.moive_comment_create, name='moive_comment_create'),
    path('<int:movie_id>/movie_comments/<int:comment_id>/comment_delete/', views.movie_comment_delete, name='movie_comment_delete'),
    path('<int:movie_id>/movie_comments/<int:comment_id>/comment_update/', views.movie_comment_update, name='movie_comment_update'),
    # 리뷰 리스트
    path('review_list/', views.review_list, name='review_list'),
    path('review_create/', views.review_create, name='review_create'),
    # 리뷰 디테일
    path('<int:movie_id>/<int:review_id>/', views.review_detail, name='review_detail'),
    path('<int:movie_id>/<int:review_id>/review_update/', views.review_update, name='review_update'),
    path('<int:movie_id>/<int:review_id>/review_delete/', views.review_delete, name='review_delete'),
    path('<int:movie_id>/<int:review_id>/review_comments/', views.review_comment_create, name='review_comment_create'),
    path('<int:movie_id>/<int:review_id>/review_comments/<int:comment_id>/comment_delete/', views.review_comment_delete, name='review_comment_delete'),
    path('<int:movie_id>/<int:review_id>/like/', views.like, name='like'),
]