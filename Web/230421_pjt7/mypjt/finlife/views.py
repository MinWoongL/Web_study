from django.shortcuts import render
from django.conf import settings
import requests, json
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import DepositProducts, DepositOptions
from .serializer import DepositOptionsSerializer, DepositProductsSerializer
from django.db.models import Max

BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'
API_KEY = settings.API_KEY
# Create your views here.

@api_view(['GET'])
def api_test(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth': API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1
        
    }
    response = requests.get(URL, params=params).json()
    return JsonResponse({'response': response})

@api_view(['GET'])
def save_deposit_products(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth': API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1
        
    }
    response = requests.get(URL, params=params).json()
    for item in response['result']['baseList']:
        serializer = DepositProductsSerializer(data=item)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
    for item in response['result']['optionList']:
        # print(item)
        for key in item.keys():
            if item[key] is None:
                item[key] = -1
        # print('11111')
        serializer = DepositOptionsSerializer(data=item)
        # item의 fin_prdt_cd로 depositproducts테이블의 일치하는 pk값을 가져와서 넣기
        # serializer 는 fin_prdt_cd 필드가 read_only 로 되었어서 받아오지 못함
        product = DepositProducts.objects.get(fin_prdt_cd=item['fin_prdt_cd'])
        # print(product)
        if serializer.is_valid(raise_exception=True):
            # print('22222')
            serializer.save(fin_prdt_cd = product)
            
            
@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == "POST":
        serializer = DepositProductsSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    products = DepositProducts.objects.all()
    serializer = DepositProductsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def deposit_products_options(request, fin_prdt_cd):
    # 주소값의 fin_prdt_cd와 같은값을 가진 product 찾기
    product = DepositProducts.objects.get(fin_prdt_cd = fin_prdt_cd)
    # 해당 product를 참조하고있는 options 역참조해서 다 찾기
    options = product.options.all()
    serializer = DepositOptionsSerializer(options, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def top_rate(request):
    # intr_rate2가 최대인 값을뽑음 => { 'top_rata': 4.0 } 형태처럼 딕셔너리형태로 필드 한개 반환
    # from django.db.models import Max 해줘야함
    top_option = DepositOptions.objects.aggregate(top_rate=Max('intr_rate2'))
    # option 모델에서 해당 intr_rate2를 가진 데이터를 가져온다
    option = DepositOptions.objects.get(intr_rate2=top_option['top_rate'])
    # 가져온 option 데이터의 fin_prdt_cd_id를 가진 product를 받아옴
    product = DepositProducts.objects.get(id = option.fin_prdt_cd_id)
    serializer_p = DepositProductsSerializer(product)
    # 가져온 예금상품을 참조하고있는 모든 옵션을 역참조로 찾음
    options = product.options.all()
    serializer_o = DepositOptionsSerializer(options, many=True)
    return Response({
        'doposit_product': serializer_p.data,
        'options': serializer_o.data,
        })
    