from django.conf.urls import url
from . import views
from django.urls import path

app_name='movie'

urlpatterns = [
    path('search/', views.MovieInfoAPIView.as_view(), name='api_search'),
    path('posts/', views.PostListAPIView.as_view(), name='allPost'),
    url(r'posts/(?P<pk>[0-9]+)/', views.MovieDetailAPIView.as_view(), name='detail'),
    #url(r'posts/(?P<pk>[0-9]+)/commnets/', views.MovieDetailAPIView.as_view(), name='detail'),


]