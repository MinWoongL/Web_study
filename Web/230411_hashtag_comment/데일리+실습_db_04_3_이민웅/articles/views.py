from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Article, Comment, Hashtag
from .forms import ArticleForm, CommentForm

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            
            # 공백으로 구분지어서 출력
            # content 의 개행을 띄어쓰기로 변경
            contents = article.content.replace('\n\r', ' ').split(' ')
            # print(contents)
            # get_or_create: 새로운 데이터는 저장/기존에 이미 있으면 가져온다
            # 반환값: 생성한 객체, 생성여부(2가지 반환)
            for content in contents:
                if content.startswith('#'):
                    # created는 사용하지않음 (나눠서 저장만 해주기 위해서 만든 것)
                    hashtag, created = Hashtag.objects.get_or_create(content = content[1:])
                    article.hashtags.add(hashtag)
            
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user: 
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')


@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)

@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk = article_pk)
        
        if article.like_users.filter(pk = request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('articles:index')
    return redirect('accounts:login')

def profile(request, username):
    # get_user_model() import 후 Users.objects 를 대체
    # filter는 조건에 맞는 모든데이터를 반환하기 때문에 first() 로 하나만 반환
    user = get_user_model().objects.filter(username = username).first()
    
    # 유저가 작성한 게시글
    articles = user.article_set.all()
    # 유저가 좋아요를 누른 게시글
    like_articles = user.like_articles.all()
    context = {
        'user': user,
        'articles':articles,
        'like_articles':like_articles,
    }
    return render(request, 'articles/profile.html', context)


def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk = hash_pk)
    articles = hashtag.article_set.all().order_by('-pk')
    context = {
        'hashtag': hashtag,
        'articles': articles,
    }
    return render(request, 'articles/hashtag.html', context)
    