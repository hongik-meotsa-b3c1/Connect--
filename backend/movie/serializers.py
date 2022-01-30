from rest_framework.serializers import ModelSerializer
from .models import MovieInfo

class MovieInfoSerializer(ModelSerializer):
    class Meta:
        model = MovieInfo
        fields = '__all__'
    