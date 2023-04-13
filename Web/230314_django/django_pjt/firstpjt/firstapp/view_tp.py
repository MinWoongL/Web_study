from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def first(request):
    # 변수를 만들고
    # template 으로 전달을 할 수 있다.
    name = 'Ethan'
    job = 'SSAFY_9기'
    menus = ['A','B','C']
    test = 'AaBbCc'
    context = {
        'name' : name,
        'job' : job,
        'menus' : menus,
        'test' : test,
    }


    return render(request, 'first.html', context)

