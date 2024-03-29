from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    # auto_now_add: 생성시에만, 현재시간을 저장
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now: 생성 시 + 수정 시에 현재 시간을 저장
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번째글 - {self.title}'
    