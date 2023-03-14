from django.shortcuts import render
from datetime import datetime
# Create your views here.

def first(request):
    # 변수를 만들고
    # template 으로 전달을 할 수 있다.
    name = 'Ethan'
    job = 'SSAFY_9기'
    menus = ['A','B','C']
    users = ['D','E','F']
    test = 'AaBbCc'
    today = datetime.now()
    context = {
        'name' : name,
        'job' : job,
        'menus' : menus,
        'test' : test,
        'users' : users,
        'today' : today
    }
    



    return render(request, 'first.html', context)
