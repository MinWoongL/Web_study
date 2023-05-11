from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import JsonResponse
from .models import Todo
from .serializers import TodoSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.

def index(request):
    return JsonResponse({ 'message': 'okay'})

@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == "GET":
        todos = get_list_or_404(Todo)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'DELETE', 'PUT'])
def todo_detail(request, todo_pk):
    todo = get_object_or_404(Todo, pk = todo_pk)
    
    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        pass
        
        
    

    