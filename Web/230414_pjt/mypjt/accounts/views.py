from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.views.decorators.http import require_http_methods
# Create your views here.
@require_http_methods(['GET','POST'])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')
    
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    
    return render(request, 'login.html', context)

@require_http_methods(['POST'])
def logout(request):
    auth_logout(request)
    return redirect('movies:index')

@require_http_methods(['GET','POST'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'signup.html', context)

@require_http_methods(['GET','POST'])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance = request.user)
        
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserChangeForm(instance = request.user)
    context = {
        'form': form,
    }
    
    return render(request, 'update2.html', context)

@require_http_methods(['POST'])
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('movies:index')

@require_http_methods(['GET','POST'])
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('movies:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'change_password.html', context)

@require_http_methods(['GET'])
def profile(request, username):
    User = get_user_model()
    user_data = User.objects.get(username = username)
    
    context = {
        'user_data': user_data,
    }
    return render(request, 'profile.html', context)

@require_http_methods(['POST'])
def follow(request, username):
    if request.user.is_authenticated:
        User = get_user_model()
        user_data = User.objects.get(pk = username)
        if user_data != request.user:
            if user_data.followers.filter(pk = request.user.pk).exists():
                user_data.followers.remove(request.user)
            else:
                user_data.followers.add(request.user)
        return redirect('accounts:profile', user_data.username)
    return redirect('accounts:login')