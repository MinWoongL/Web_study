from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # symmetrical = 한 쪽이 관계를 가져도 반대쪽에서 꼭 가질 필요는 없다.
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
