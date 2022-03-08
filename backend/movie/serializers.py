from rest_framework.serializers import ModelSerializer
from .models import MovieInfo, MoviePost, Comment
from django.contrib.auth import get_user_model

class MovieInfoSerializer(ModelSerializer):
    class Meta:
        model = MovieInfo
        fields = ['id', 'movie_title', 'movie_director', 'movie_pubDate', 'movie_image']


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username','nickname']

class MoviePostSerializer(ModelSerializer):
    author = AuthorSerializer(read_only = True)

    class Meta:
        model=MoviePost
        fields='__all__'
    

class CommentSerializer(ModelSerializer):
    author = AuthorSerializer(read_only = True)
    print("CommnetSerializer동작")

    class Meta:
        model = Comment
        fields=['id','author', 'message','created_at']
    