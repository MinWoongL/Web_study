from rest_framework import serializers
from .models import Article, Comment

# Form -> forms.Form / forms.ModelForm
# serializers -> Serializer / ModelSerializer

# Model 이 붙으면 -> 정의한 필드에 대해서 입출력
# 안붙으면 -> 사용자가 원하는 필드를 추가로 입력 받거나, 출력함

# class ArticleListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'


# ModelSerializer 에서는 추가적인 field 사용은 불가능함
# Serializer 사용
# 정의된 필드 외의 필드를 사용자로부터 입력받고 싶을 때
class ArticleListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()
    # 입력을 받지 않고 출력만 하길 원할 때
    created_at = serializers.DateTimeField(read_only=True)
    # write_only: 입력만 받고, 출력을 하길 원하지 않을 때
    # required: 반드시 입력받아야하면 True
    # allow_blank: blank 허용
    # aloow_null: null 값 허용
    myfield = serializers.CharField(write_only=True, required=False, allow_blank=True, allow_null=True)
    # -> post요청시 request.data 까지는 들어가고 valid 검사 후에는 포함되지 않음
    
    
    # BaseSerializer 의 create() 함수가 호출됨
    # serializers.Serializer 사용 시, create 를 반드시 재정의 해야함
    def create(self, validated_data):
        print('validated_data = ', validated_data)
        # 여기서 myfield에 대한 연산
        # ex -> validated_data['title'] += validated_data['myfield']
        return Article.objects.create(
            title=validated_data['title'],
            content=validated_data['content']
        )
    
    def update(self, instance, validated_data):
        # 수정한 값을 받아서 있다면 get에서 'title', 없다면 instance.title
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance