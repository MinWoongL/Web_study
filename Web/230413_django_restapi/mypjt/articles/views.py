from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serializers import ArticleListSerializer
from .models import Article, Comment
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# 전체조회, 생성
# @api_view: 함수가 API View 로 동작하도록 반환
#   - 메소드 제한 기능
#   - HttpResponse 대신 Json 이나 DRF 의 Response 객체 반환 가능
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'POST':
        serializer = ArticleListSerializer(data = request.data)
        # valid 하지 못할 때, 바로 에러 띄워서 반환 -> raise_exception
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    # GET 이라면
    articles = Article.objects.all()
    # serializer: 쉽게 말하면 원하는 형태로 포장하는 것
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)
    # return JsonResponse({"message":"okay"})
    


# 상세조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'PUT':
        serializer = ArticleListSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # 에러문구 보기싫다면 get_object_or_404 활용
    
    # article = Article.objects.get(pk=pk)
    serializer = ArticleListSerializer(article)
    return Response(serializer.data)