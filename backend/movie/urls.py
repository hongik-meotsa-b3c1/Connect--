from django.conf.urls import url
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name='movie'

router = DefaultRouter()
router.register(r'posts/(?P<post_pk>\d+)/comments', views.CommentViewSet)




urlpatterns = [
    
    path('search/', views.MovieInfoAPIView.as_view(), name='api_search'),  
    path('posts/', views.PostListAPIView.as_view(), name='allPost'),

    # 밑에 두개 순서바꾸면 안됨!!
    path("", include(router.urls)), 
    url(r'posts/(?P<pk>[0-9]+)/', views.MovieDetailAPIView.as_view(), name='detail'),
    
    
]