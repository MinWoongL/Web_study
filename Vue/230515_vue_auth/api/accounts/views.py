from django.shortcuts import render
from dj_rest_auth.registration.views import RegisterView as DefaultRegisterView
from rest_framework import status
from rest_framework.response import Response

# class CustomRegisterView(DefaultRegisterView):
#     def create(self, request, *args, **kwargs):
#         # 기존 RegisterView의 create 메서드를 오버라이드하여 원하는 동작을 추가/수정
#         nickname = request.data.get('nickname')  # nickname 필드 값 가져오기
#         # nickname 필드를 원하는 방식으로 처리
#         # 예: User 모델에 저장, 프로필 생성 등

#         return super().create(request, *args, **kwargs)  # 원래의 create 메서드 호출



# Create your views here.
