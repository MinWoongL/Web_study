from django.shortcuts import render, redirect
from .models import Movie
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .forms import MovieForm
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
            form.save()
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
    
    context = {
        'movie' : data,
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