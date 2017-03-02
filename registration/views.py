from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User


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
    return redirect('home.html')


def login_view(request):
    return render(request, 'login.html')
