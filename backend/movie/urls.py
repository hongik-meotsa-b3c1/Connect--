from django.conf.urls import url
from . import views
from django.urls import path

app_name='movie'

urlpatterns = [
    path('search/', views.MovieInfoAPIView.as_view(), name='api_search'),
    path('postWrite/', views.PostWrite.as_view(), name='postWrite'),
    # url(r'(?P<pk>[0-9]+)/', views.MovieDetailAPIView.as_view(), name='detail'),
    

]