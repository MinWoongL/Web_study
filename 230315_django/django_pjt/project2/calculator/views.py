from django.shortcuts import render

# Create your views here.
def calcul(request, num, num2):
    r1 = num + num2
    r2 = num - num2
    r3 = num * num2
    if num2 != 0:
        r4 = num/num2
    else:
        r4 = 0

    context = {
        'num1':num,
        'num2':num2,
        'r1': r1,
        'r2' : r2,
        'r3': r3,
        'r4': r4,
    }

    return render(request, 'cal.html', context)
        

