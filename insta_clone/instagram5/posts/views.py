from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.views.decorators.http import require_http_methods
# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    
    context = {
        'form':form
    }
    return render(request, 'posts/form.html', context)

@require_http_methods(['POST'])
def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    
    return redirect("posts:index")

@require_http_methods(['GET','POST'])
def update(request, pk):
    post = Post.objects.get(pk=pk)
    print('startstartstart')
    if request.method == "POST":
        print('<<<<<<<<<<<<<<<<<<<<<')
        form = PostForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            form.save()
            return redirect('posts:index')
    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'posts/form.html', context)
    