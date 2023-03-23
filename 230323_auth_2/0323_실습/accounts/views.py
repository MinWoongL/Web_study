from django.shortcuts import render, redirect
# 로그인 전용 form module
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
# 변수랑 이름 똑같아서 as로 별명 지어줌
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.views.decorators.http import require_http_methods, require_POST


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        messages.info(request, '이미 로그인중입니다.')
        return redirect('articles:index')
    if request.method == "POST":
        # 로그인 처리를 해줌
        # 과정
        # 1. 비어있는 아이디와 패스워드 체크
        # 2. 세션 처리
        # 3. 쿠키에 담아서 전송

        # 로그인 로직 : 위의 과정 순서대로
        # user 이름이 채워진 폼
        # 1. form으로 데이터를 받아줌
        form = AuthenticationForm(request, request.POST)
        # 아이디와 패스워드가 유효한지 검사, 유효하다면 세션에 저장, 세션아이디를 쿠키에 담아서 응답으로 보냄
        # 2. 유효성 검사
        # print('<<<<<<<<<<<')
        if form.is_valid():
            # 세션 데이터를 생성하는 코드
            # 3. 로그인
            #  1) django-session 데이터 추가
            #  2) cookie 세션 id 추가
            # print('>>>>>>>>>>>>>>>>>>>')
            auth_login(request, form.get_user())
            
            return redirect(request.GET.get('next') or 'articles:index')
        # 맨 처음 로그인 화면 다시 줘
    else:
        # 비어있는 로그인 페이지를 제공
        # 원래는 forms.py만들어서 가져와야하는데 장고가 제공해 준 아래 포맷 가져오는 것
        form = AuthenticationForm()
        # next = request.GET.get('next')
    
    context = {
        # 'next': next,
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def signup(request):
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

# POST요청만 허용
@require_POST
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')

# 함수가 특정한 요청 method만 허용하도록 하는 데코레이터
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance = request.user)
    context = {
        'form': form,
    }

    return render(request, 'accounts/update.html', context)

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        # form = PasswordChangeForm(user=request.user, data = request.POST)
        # 변경 후 기존세션과의 정보가 일치하지 않아 로그인이 유지되지 못함
        if form.is_valid():
            form.save()
            # 암호가 변경되어도 로그아웃 되지 않도록 새로운 password의 session data로 session을 업데이트
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/change_password.html', context)



