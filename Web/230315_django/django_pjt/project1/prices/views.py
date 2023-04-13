from django.shortcuts import render

# Create your views here.

def prices(request, thing, cnt):

    product_price = {
        '칙촉' : 6900,
    }
    ans = 0
    if thing in product_price.keys():
        ans = product_price[thing]
    context = {
        'thing': thing,
        'cnt': cnt,
        'ans' : ans,
    }
    

    return render(request, 'price.html', context)
