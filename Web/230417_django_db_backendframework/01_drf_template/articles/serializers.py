from rest_framework import serializers
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        # 해당 필드를 유효성 검사에서 제외시키고 데이터 조회시에는 출력
        read_only_fields = ('article',)
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop('article', None)
        return rep
    

class ArticleListSerializer(serializers.ModelSerializer):
    # 게시글의 댓글을 모두 조회?
    # 1. CommentSerializer 를 포함시키는 것: Nested Serializer
    #   - Article 모델이 알고 있는 필드만 사용 가능
    #       즉, 참조 및 역참조 관계에 있는 데이터만 가져올 수 있다.
    
    # comments = CommentSerializer(many=True, read_only=True)
    # comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    
    # 위 처럼 특정 필드를 override 혹은 추가한 경우에는 read_only_fields 가 동작하지 않는다.
    class Meta:
        model = Article
        fields = ('id', 'title', 'content')
        # 불가능
        # read_only_fields = ('comments', 'comment_count',)
        
        
    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['comments'] = rep.pop('comments', [])
        # print(instance)
        # ori_rlt = super().to_representation(instance)
        # print(ori_rlt)
        # return rep


# 상속 이용하기
class ArticleDetailSerializer(ArticleListSerializer):
    comments = CommentSerializer(many=True, read_only = True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    
    class Meta(ArticleListSerializer.Meta):
        fields = ArticleListSerializer.Meta.fields + (
            'comments',
            'comment_count'
        )
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments'] = rep.pop('comments', [])
        # print(instance)
        # ori_rlt = super().to_representation(instance)
        # print(ori_rlt)
        return rep

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = '__all__'
        

    