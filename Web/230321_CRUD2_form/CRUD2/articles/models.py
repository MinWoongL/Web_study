from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20, null=False)
    content = models.TextField()
    author = models.TextField(default="user")
    # upload_to = 미디어파일 관리를 위해 경로를 추가설정
    image = models.ImageField(blank=True, upload_to='articles/%Y%m%d')

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
