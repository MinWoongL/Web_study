from django.shortcuts import render
from datetime import datetime
import random
from django.http import HttpResponse
# Create your views here.

def second(request):
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


    return render(request, 'secondapp/second.html', context)

def greeting(request):
    foods = ['apple', 'banana', 'coconut', 'ham',]
    pick = random.choice(foods)
    info = {
        'name' : 'Alice'
    }
    context = {
        'foods' : foods,
        'info': info,
        'pick': pick,
    }

    return render(request, 'secondapp/greeting.html', context)

def greeting2(request):
    foods = ['apple', 'banana', 'coconut', 'ham',]
    pick = random.choice(foods)
    info = {
        'name' : 'Alice'
    }
    context = {
        'foods' : foods,
        'info': info,
        'pick': pick,
    }

    return render(request, 'secondapp/greeting2.html', context)

def index(request):
    
    return render(request, 'secondapp/index.html')

def catch(request):

    context = {
        'name' : request.GET.get('message'),
    }
    

    return render(request, 'secondapp/catch.html', context)

def catchtest(request):
    

    return render(request, 'secondapp/2-2.html')

def introduce(request, name, age):
    
    context = {
        'name' : name,
        'age' : age,
    }

    return render(request, 'secondapp/introduce.html', context)

def detail(request, x):
    foods = ['apple', 'banana', 'coconut', 'ham',]
    pick = random.choice(foods)
    info = {
        'name' : 'Alice'
    }
    context = {
        'x': x,
        'foods' : foods,
        'info': info,
        'pick': pick,
    }
    
    if x.isdigit():
        return render(request, 'secondapp/detail.html', context)
    else:
        return render(request, 'secondapp/detail2.html', context)

# def detail2(request, name):
#     foods = ['apple', 'banana', 'coconut', 'ham',]
#     pick = random.choice(foods)
#     info = {
#         'name' : 'Alice'
#     }
#     context = {
#         'name': name,
#         'foods' : foods,
#         'info': info,
#         'pick': pick,
#     }
#     return render(request, 'secondapp/detail2.html', context)