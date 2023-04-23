from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serializers import BookListSerializer, BookSerializer, BookDetailSerializer, CommentSerializer
from .models import Book, Comment

@api_view(['GET', 'POST'])
def book_list(request):
    # Q 1.
    books = Book.objects.all()
    if request.method == "GET":
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
    
    # Q 2.
    elif request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'DELETE', 'PUT'])
def book_detail(request, book_pk):
    book = Book.objects.get(id = book_pk)
    if request.method == "GET":
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "PUT":
        serializer = BookDetailSerializer(book, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def comment_list(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    if request.method == "GET":
        comments = book.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(book=book)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# @api_view(['POST'])
# def comment_create(request, book_pk):
#     book = get_object_or_404(Book, pk=book_pk)
#     serializer = CommentSerializer(book, data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(book=book)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    