from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}번째글 - {self.title}'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content
    

# # views.py
# comment = Comment.objects.get(pk = comment_pk)

# # 정참조: 외래키를 가지고 있는 쪽에서 참조하는 방법
# comment.article.~~~~

# # 실수 주의
# Comment.article.title

# # 역참조: 참조당하는 쪽에서 데이터를 조회하는 방법
# article = Article.objects.get(pk = article_pk)

# article.comment_set.all()
# article.comment_set.filter() 등등