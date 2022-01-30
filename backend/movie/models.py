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
    USER_ID = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    post_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    movie_image = models.ImageField(upload_to='')
    content = models.CharField(max_length=500)
    NumOfPeople = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gather_date = models.DateTimeField(blank = False, null = False)

    def __str__(self):
        return self.post_id
