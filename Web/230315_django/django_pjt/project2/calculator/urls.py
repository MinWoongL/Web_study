from django.contrib import admin
from django.urls import path
from calculator import views

urlpatterns = [
    path('<int:num>/<int:num2>/', views.calcul),
    
]
