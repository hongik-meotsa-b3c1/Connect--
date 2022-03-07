from django.db import models
from django.conf import settings

# Create your models here.
class MovieInfo(models.Model): 
    movie_title = models.CharField(max_length=30)
    movie_image = models.CharField(max_length=30)
    movie_link = models.CharField(max_length=30)
    movie_director = models.CharField(max_length=30)
    movie_pubDate = models.CharField(max_length=20)
    movie_userRating = models.FloatField()
    movie_actor=models.CharField(null=False,max_length=1000,default='')
    def getTitle(self):
    	return self.movie_title


class MoviePost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="my_post_set", on_delete=models.CASCADE)
    title = models.CharField(max_length=30) # 글제목
    content = models.CharField(max_length=700) # 글내용
    movie_title = models.CharField(max_length=700)
    movie_image = models.CharField(max_length=100) # 글 이미지 url
    movie_link = models.CharField(max_length=100) # 영화정보 상세 url
    NumOfPeople = models.IntegerField() # 모집인원
    gather_date = models.DateTimeField(blank = False, null = False) #모집날짜
    movie_director = models.CharField(null=False,max_length=1000,default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(MoviePost, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ["-id"]

 
