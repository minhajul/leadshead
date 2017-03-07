from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_view(request):
    return render(request, 'login.html')


@csrf_protect
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Something went wrong")
                return redirect('login')
        else:
            messages.error(request, "Authentication Failed!")
            return redirect('login')
    else:
        return redirect('login')


def logout_user(request):
    logout(request)
    return redirect('/')


def register_view(request):
    return render(request, 'register.html')


@csrf_protect
def register_user(request):
    User.objects.create_user(
        username=request.POST['username'],
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=request.POST['password'],
    )
    messages.success(request, 'Registration Success')
    return redirect('home.html')


@login_required
def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('/')

    return render(request, 'profile.html', {'user_profile': user})
