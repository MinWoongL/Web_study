from django.shortcuts import render, redirect
from .models import Article
# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)

def detail(request, pk):
    # 항상 POST를 먼저 확인하고 GET을 나중에
    article = Article.objects.get(pk = pk)
    if request.method == "POST":
        article.delete()
        return redirect('articles:index')
        
    elif request.method == 'GET':
        context = {
            'article': article,
        }

        return render(request, 'articles/detail.html', context)

# def new(request):
#     return render(request, 'articles/new.html')

def create(request):
    if request.method == 'POST':
        # 저장 코드
        title = request.POST.get('title')
        content = request.POST.get('content')

        # 1.
        # article = Article()
        # article.title = title
        # article.content = content
        # article.save()

        # 2
        article = Article(title=title, content=content)
        article.save()

        # 3
        # Article.objects.create(title=title, content=content)

        return redirect('articles:detail', article.pk)
    else:
        return render(request, 'articles/create.html')

def delete(request, pk):
    article = Article.objects.get(pk = pk)
    if request.method == 'POST':
        article.delete()

        return redirect('articles:index')
    else:
        redirect('articles:detail', article.pk)

# def edit(request, pk):
#     article = Article.objects.get(pk = pk)
#     context = {
#         'article': article,
#     }
#     return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk = pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:index')
    else:
        # 기존 내용(context) 주고 수정
        context = {'article': article}
        return render(request, 'articles/update.html', context)