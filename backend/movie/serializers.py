from rest_framework.serializers import ModelSerializer
from .models import MovieInfo, MoviePost

class MovieInfoSerializer(ModelSerializer):
    class Meta:
        model = MovieInfo
        fields = ['id', 'movie_title', 'movie_director', 'movie_pubDate']


class MoviePostSerializer(ModelSerializer):
    class Meta:
        model=MoviePost
        fields='__all__'
    