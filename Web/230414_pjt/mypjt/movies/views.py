from django.shortcuts import render, redirect
from .models import Movie, Comment
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from .forms import MovieForm, CommentForm
# Create your views here.

@login_required
def index(request):
    movies = Movie.objects.all()
    
    context = {
        'movies' : movies,
    }
    
    return render(request, 'index.html', context)

@require_http_methods(['GET','POST'])
def create(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:index')
    else:
        form = MovieForm()
    context = {
        'form' : form,
    }
    return render(request, 'create.html', context)

@require_http_methods(['GET'])
def detail(request, pk):
    data = Movie.objects.get(pk = pk)
    comment_form = CommentForm()
    comments = data.comment_set.all()
    
    context = {
        'movie' : data,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    
    return render(request, 'detail.html', context)

@require_http_methods(['GET','POST'])
def update(request, pk):
    movie = Movie.objects.get(pk = pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance = movie)
    
    context = {
        'form' : form,
        'movie' : movie,
    }
    return render(request, 'update.html', context)

@require_http_methods(['POST'])
def delete(request, pk):
    movie = Movie.objects.get(pk = pk)
    movie.delete()
    return redirect('movies:index')

@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk = pk)
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie_id = movie
            comment.user = request.user
            comment.save()
        return redirect('movies:detail', movie.pk)
    return request('accounts:login')

@require_POST
def comments_delete(request, movie_pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk = comment_pk)

        if comment.user == request.user:
            comment.delete()
        return redirect('movies:detail', movie_pk)
    return redirect('accounts:login')

@require_POST
def likes(request, pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=pk)
        if movie.like_users.filter(pk = request.user.pk).exists():
            movie.like_users.remove(request.user)
        else:
            movie.like_users.add(request.user)
        return redirect('movies:index')
    return redirect('accounts:login')
