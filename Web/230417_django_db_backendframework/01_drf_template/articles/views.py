from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer, ArticleDetailSerializer

from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
# PageNumberPagination: page size 기반의 pagination
# LimitOffsetPagination: Limit 외 offset 기반으로 pagination

from drf_yasg.utils import swagger_auto_schema


# Create your views here.
# @api_view(['GET'])
# def article_list(request):
#     articles = Article.objects.all()
#     serializer = ArticleListSerializer(articles, many=True)
#     return Response(serializer.data)

# DRF에서 api_view 데코레이터는 필수로 작성해야함
# -> DRF view 함수가 응답해야하는 HTTP 메서드 목록을받음
# -> 기본적으로 GET 메서드만 허용되며 다른 메서드 요청에 대해서는 405 Method Not Allowed로 응답

@swagger_auto_schema(methods=['POST'], request_body=ArticleListSerializer)
@api_view(['GET', 'POST'])
def article_list(request):
    # if request.method == 'GET':
    #     articles = get_list_or_404(Article)
    #     serializer = ArticleListSerializer(articles, many=True)
    #     return Response(serializer.data)
    # elif request.method == 'POST':
    #     serializer = ArticleSerializer(data = request.data)
    #     print('>>>>>>>>>>>>>>>>>>>>')
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        serializer = ArticleListSerializer(data=request.data)
        # raise_exception: is_valid 하지 않을 때 에러를 띄우기 위해
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    # Pagination
    articles = Article.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 5
    # pagination 을 한 쿼리셋으로 변경
    paginated_articles = paginator.paginate_queryset(articles, request)
    # 해당 쿼리셋을 기준으로 serializer를 만듦
    serializer = ArticleListSerializer(paginated_articles, many=True)
    # paginator 를 이용하여, pagination 이 완료된 결과 반환
    # return Response(serializer.data)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == 'GET':
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        # 삭제는 따로 반환할 데이터가 없기 때문에
        # 204: 요청완료 + 반환할 데이터 없음
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        # 기존의 article에 데이터 넣고(수정)
        serializer = ArticleDetailSerializer(article, data=request.data)
        # 유효하지 않은 데이터에 대해 예외 발생시키기, 기본적으로 HTTP 400
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET', 'POST'])
def comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk = comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)