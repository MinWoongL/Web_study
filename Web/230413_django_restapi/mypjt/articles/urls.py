from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'articles'
urlpatterns = [
    # RESTful 한 상태 -> 식별자와 행위를 구분해야함
    # 잘못된 URL 구성
    # path('', views.index, name='index'), # GET
    # path('create/', views.create, name='create'), # PUT
    # path('<int:pk>/', views.detail, name='detail'),
    # path('<int:pk>/update/', views.update, name='update'),
    # path('<int:pk>/delete', views.delete, name='delete'),
    
    
    # RestAPI
    path('', views.article_list),
    path('<int:pk>/', views.article_detail),
]
