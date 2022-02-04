from rest_framework.serializers import ModelSerializer
from .models import MovieInfo, MoviePost

class MovieInfoSerializer(ModelSerializer):
    class Meta:
        model = MovieInfo
        fields = '__all__'


class MoviePostSerializer(ModelSerializer):
    class Meta:
        model=MoviePost
        fields='__all__'
    