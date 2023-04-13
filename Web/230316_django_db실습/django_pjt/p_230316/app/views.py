from django.shortcuts import render

# Create your views here.

def index(request):


    return render(request, 'app/index.html')

def throw(request):


    return render(request, 'app/throw.html')

def catch(request):

    message = request.GET.get('message')
    context = {
        'message' : message,
    }

    return render(request, 'app/catch.html', context)