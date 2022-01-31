import json
import urllib.request
from django.conf import settings
from .models import MovieInfo
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import MovieInfoSerializer
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404


class MovieInfoAPIView(APIView):

    def get(self,request):
            config_secret_debug = json.loads(open(settings.SECRET_DEBUG_FILE).read())
            client_id = config_secret_debug['NAVER']['CLIENT_ID']
            client_secret = config_secret_debug['NAVER']['CLIENT_SECRET']
            q = request.GET.get('q')
            encText = urllib.parse.quote("{}".format(q))
            url = "https://openapi.naver.com/v1/search/movie?query=" + encText  # json 결과
            movie_api_request = urllib.request.Request(url)
            movie_api_request.add_header("X-Naver-Client-Id", client_id)
            movie_api_request.add_header("X-Naver-Client-Secret", client_secret)
            response = urllib.request.urlopen(movie_api_request)
            rescode = response.getcode()
            if (rescode == 200):
                response_body = response.read()
                result = json.loads(response_body.decode('utf-8'))
                items = result.get('items')

                context = {
                    'items':items
                }
                try:
                    qs = MovieInfo.objects.all()
                    qs.delete()
                    
                    for item in items:
                        _MovieInfo = MovieInfo()
                        _MovieInfo.movie_title=item.get('title').strip('</b>')
                        _MovieInfo.movie_link=item.get('link')
                        _MovieInfo.movie_director=item.get('director').split('|')[0]
                        _MovieInfo.movie_pubDate=item.get('pubDate')
                        _MovieInfo.movie_image=item.get('image')
                        _MovieInfo.movie_userRating=item.get('userRating')
                        _MovieInfo.save()
                        
                    
                    qs = MovieInfo.objects.all()
                    serializer = MovieInfoSerializer(qs, many = True)
                    return Response(serializer.data)  


                except:
                    print("error")
                    return Response(serializer.errors)


class MovieDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return MovieInfo.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieInfoSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MovieInfoSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        
             
                  
                


    

 

