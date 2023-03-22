from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }

    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        # 인코딩 되지않은 이미지 파일은 request.FILES 에 들어옴
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            # cleaned_data: form의 데이터를 파이썬 딕셔너리로 반환
            # Model을 사용했을때 방법
            # data = form.cleaned_data
            # 만약 제목:<사용자입력> 형식으로 받고싶다면
            # data['title'] = '제목:' + data['title']
            # article = Article(**data)
            # article.save()
            article = form.save()
        # title = request.POST.get('title')
        # content = request.POST.get('content')

        # article = Article(title=title, content=content)
        # article.save()

            # 유효성 검사 통과하면 상세페이지로
            return redirect('articles:detail', article.pk)
        # 통과하지 못하면 작성페이지로
        # return redirect('articles:create')
    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'articles/create.html', context)
    
def detail(request, pk):
    article = Article.objects.get(pk = pk)

    if request.method == "POST":
        article.delete()
        return redirect('articles:index')
    else:
        context = {
            'article' : article,
        }

        return render(request, 'articles/detail.html', context)
    
def delete(request, pk):    
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        article.delete()

        return redirect('articles:index')
    else:
        redirect('articles:detail', article.pk)

def update(request, pk):
    article = Article.objects.get(pk = pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
        # article.title = request.POST.get('title')
        # article.content = request.POST.get('content')
        # article.save()
        return redirect('articles:index')
    else:
        form = ArticleForm(instance=article)
    context = {
        'form' : form,
        'article': article,
        }
    return render(request, 'articles/update.html', context)
