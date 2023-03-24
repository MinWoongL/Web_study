from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release_date = models.DateField(auto_now=False)
    genre_choice = (('Comedy', 'Comedy'),('horror', 'horror'),('Romance', 'Romance'))
    genre = models.CharField(max_length=30, choices=genre_choice)
    score = models.FloatField(validators=[MaxValueValidator(5, '0~5 사이 평점'), MinValueValidator(0, '0~5 사이 평점')])
    poster_url = models.CharField(max_length=50)
    description = models.TextField()

    actor_image = models.ImageField(blank=True, upload_to='movies/%Y%m%d')