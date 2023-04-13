from django.shortcuts import render, redirect
from .models import Question, Comment
from .forms import QuestionForm, CommentForm
from django.db.models import Max, Avg
import random as rd

# Create your views here.

def index(request):
    questions = Question.objects.all()
    context = {
        'questions' : questions,
    }
    return render(request, 'eithers/index.html', context)


def create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('eithers:index')
    else:
        form = QuestionForm()
    
    context = {
        'form' : form
    }
    
    return render(request, 'eithers/create.html', context)

def detail(request, question_pk):
    question = Question.objects.get(pk = question_pk)
    comment_form = CommentForm()
    comments = question.comments.all()
    context = {
        'question': question,
        'comment_form' : comment_form,
        'comments': comments,
    }
    return render(request, 'eithers/detail.html', context)

def comment(request, question_pk):
    question = Question.objects.get(pk = question_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        # 사용자가 직접 question 을 입력하지 않으므로
        # views.py 에서 지정해준 후 저장
        comment = form.save(commit=False)
        comment.question = question
        comment.save()
    return redirect('eithers:detail', question_pk)


def random(request):
    # questions = Question.objects.all()
    count = Question.objects.count()
    if count <= 0:
        return redirect('eithers:index')
    # 첫 번째 방법 - 가장 쉬운 방법(전부 가져와서 하나 고르기)
    # question = rd.choice(Question.objects.all())
    # return redirect('eithers:detail', question.id)
    
    # 두 번째 방법 -> 정렬하고 하나만 반환 -> 더 빠르다
    # question = Question.objects.order_by('?').first()
    # return redirect('eithers:detail', question.id)
    
    # 데이터가 적을 때 일반적으로 사용
    # max_id 기준으로 randint 사용하기
    # max_id = Question.objects.all().aggregate(max_id=Max('id'))['max_id']
    # from django.db.models import Max, Avg 등등
    # 조회 후 게시글이 있다면 redirect 해야함
    # if Question.objects.filter(pk = question_pk).exists():
    #   return redirect('eithers:detail', question_pk)
    # else:
    #   return redirect('eithers:random)
    num = Question.objects.all().aggregate(max_id=Max('id'))['max_id']
    r_num = rd.randint(1, num)
    if Question.objects.filter(pk = r_num).exists():
        question = Question.objects.get(pk = r_num)
        return redirect('eithers:detail', question.pk)
    else:
        return redirect('either:random')
   
    
    