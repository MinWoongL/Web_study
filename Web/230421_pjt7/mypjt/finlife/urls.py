from . import views
from django.contrib import admin
from django.urls import path, include

app_name = 'finlife'
urlpatterns = [
    path('api_test/', views.api_test, name='api_test'),
    path('save-deposit-products/', views.save_deposit_products, name='save-deposit'),
    path('deposit-products/', views.deposit_products, name='deposit-products'),
    path('deposit-products-options/<str:fin_prdt_cd>/', views.deposit_products_options, name='deposit-products-options'),
    path('deposit-products/top_rate/', views.top_rate, name='top_rate'),
    
]
