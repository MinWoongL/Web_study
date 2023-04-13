from django.urls import path
from . import views

urlpatterns = [
    path('', views.greeting2),
    path('<str:x>/', views.detail),
    # path('<int:x>/', views.detail),
]
