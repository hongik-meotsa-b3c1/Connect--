from django.db import models

# Create your models here.
class MovieInfo(models.Model): 
    movie_title = models.CharField(max_length=30)
    movie_image = models.CharField(max_length=30)
    movie_link = models.CharField(max_length=30)
    movie_director = models.CharField(max_length=30)
    movie_pubDate = models.CharField(max_length=20)
    movie_userRating = models.FloatField()
    
    def __str__(self):
    	return self.movie_title


class MoviePost(models.Model):
    USER_ID = models.ForeignKey('accounts.user', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    title = models.CharField(max_length=30) # 글제목
    content = models.CharField(max_length=700) # 글내용
    movie_title = models.CharField(max_length=700)
    movie_image = models.CharField(max_length=100) # 글 이미지 url
    movie_link = models.CharField(max_length=100) # 영화정보 상세 url
    NumOfPeople = models.IntegerField() # 모집인원
    gather_date = models.DateTimeField(blank = False, null = False) #모집날짜

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
#title content movie에 대한 pk NumOfPeople gather_data, username
 
