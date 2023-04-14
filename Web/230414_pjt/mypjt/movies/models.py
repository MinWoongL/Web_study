from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="movie_users")
    
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_users")


class Comment(models.Model):
    content = models.CharField(max_length=50)   
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comment_users")