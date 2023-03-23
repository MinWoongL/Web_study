from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# 데코레이터, 꾸밀 때 사용
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.urls import reverse

# Create your views here.
# require_GET : GET 허용, require_safe : GET, HEAD 허용
# HEAD method
# - HTTP Body 부분을 제외한 HEAD 부분만 반환 -> GET보다 빠름
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    # index 화면으로 리다이렉션
    response = render(request,"articles/index.html", context)
    # set_cookie : 응답 쿠키에 데이터를 포함시킨다
    # set_cookie(key, value,)
    response.set_cookie('message', 'cookie')
    return response
    # return render(request, 'articles/index.html', context)

@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)

@login_required
def create(request):
    # 로그인되지 않은 사용자는 로그인페이지로 리다이렉션
    # 1. 쿠키에 세션 데이터가 있는가?
    # if not request.COOKIES.get('sessionid'):
    #     return redirect('accounts:login')
    
    # 2. request.user 가 있는가?
    # 장고에서는 유저 정보를 request.user 안에 담고있다.
    if not request.user.is_authenticated:
        # return redirect(f'/accounts/login?next={request.path}')
        # reverse: 전달받은 Name에 매칭된 url 을 문자열로 반환
        # return redirect(reverse('accounts:login' + f'?next={request.path}'))
        return redirect('accounts:login')

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()

    context = {'form': form}
    return render(request, 'articles/create.html', context)

@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {'form': form, 'article': article}
    return render(request, 'articles/update.html', context)
