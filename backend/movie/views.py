from distutils.log import error
import json
from turtle import title
import urllib.request
from django.conf import settings
from .models import MovieInfo,MoviePost,Comment
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import MovieInfoSerializer,MoviePostSerializer,CommentSerializer
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import AllowAny


class MovieInfoAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self,request):
            config_secret_debug = json.loads(open(settings.SECRET_DEBUG_FILE).read())
            client_id = config_secret_debug['NAVER']['CLIENT_ID']
            client_secret = config_secret_debug['NAVER']['CLIENT_SECRET']
            print(request.body)
            req = json.loads(request.body.decode('utf-8'))
            q = req[ 'moviename']
            print(q)
            encText = urllib.parse.quote("{}".format(q))
            url = "https://openapi.naver.com/v1/search/movie?yearfrom=2022&yearto=2022&query=" + encText  # json 결과
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
                        _MovieInfo.movie_title=item.get('title').replace("<b>", "").replace("</b>", "")
                        _MovieInfo.movie_link=item.get('link')
                        _MovieInfo.movie_director=item.get('director').split('|')[0]
                        _MovieInfo.movie_pubDate=item.get('pubDate')
                        _MovieInfo.movie_image=item.get('image')
                        _MovieInfo.movie_userRating=item.get('userRating')
                        _MovieInfo.movie_actor=item.get('actor')
                        _MovieInfo.save()
                        
                    
                    qs = MovieInfo.objects.all()
                    serializer = MovieInfoSerializer(qs, many = True)
                    return Response(serializer.data)  


                except:
                    print("error")
                    return Response(serializer.errors)
    

    
class PostListAPIView(APIView):
    permission_classes = [AllowAny]

    
    def get(self, request):
        serializer = MoviePostSerializer(MoviePost.objects.all(), many=True)
        return Response(serializer.data)

    def post(self,request):
            config_secret_debug = json.loads(open(settings.SECRET_DEBUG_FILE).read())
            client_id = config_secret_debug['NAVER']['CLIENT_ID']
            client_secret = config_secret_debug['NAVER']['CLIENT_SECRET']
            req = json.loads(request.body.decode('utf-8'))
            q = req['movie_id']
            # MovieInfo db에서 movie_id 가진 객체 탐색
            movie=MovieInfo.objects.get(pk=q)
            moviename=movie.getTitle()
            print(moviename)
            encText = urllib.parse.quote("{}".format(moviename))
            url = "https://openapi.naver.com/v1/search/movie?yearfrom=2022&yearto=2022&query=" + encText  # json 결과
            movie_api_request = urllib.request.Request(url)
            movie_api_request.add_header("X-Naver-Client-Id", client_id)
            movie_api_request.add_header("X-Naver-Client-Secret", client_secret)
            response = urllib.request.urlopen(movie_api_request)
            rescode = response.getcode()
            if (rescode == 200):
                response_body = response.read()
                result = json.loads(response_body.decode('utf-8'))
                items = result.get('items')
                context = {'items':items }
                try:
                    for item in items:
                        # print('for문실행')
                        _MoviePost = MoviePost()
                        _MoviePost.author = self.request.user
                        _MoviePost.title=req['title']
                        _MoviePost.content=req['content']
                        _MoviePost.NumOfPeople=req['NumOfPeople']
                        _MoviePost.gather_date=req['gather_date']
                        _MoviePost.movie_title=item.get('title').strip('</b>')
                        _MoviePost.movie_link=item.get('link')
                        _MoviePost.movie_image=item.get('image')    
                        _MoviePost.movie_director=item.get('director')
                        _MoviePost.save()

                    MoviePost_last = MoviePost.objects.last()
                    MoviePost_id = MoviePost_last.id
                        
                    return Response(MoviePost_id)  

                except:
                    print("error")
                    return Response(error)

    
                    
   
class MovieDetailAPIView(APIView):
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return MoviePost.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        movie = self.get_object(pk)
        
        serializer = MoviePostSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MoviePostSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        movie = self.get_object(pk)
        print('작동')
        print(movie)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    
class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(post__pk=self.kwargs["post_pk"])
        return qs

    def perform_create(self, serializer):
        post = get_object_or_404( MoviePost, pk=self.kwargs["post_pk"])
        serializer.save(author=self.request.user, post=post)
        return super().perform_create(serializer)


        
             
                  
                


    

 

