from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def login(request):
    if request.method == 'POST':
        # Get form values
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        # Check for credentials
        if user is None:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

        auth.login(request, user)
        messages.success(request, 'You are now logged in')
        return redirect('dashboard')
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if passwords match
        if password != password2:
            messages.error(request, 'Password donot match')
            return redirect('register')

        # Check username
        if User.objects.filter(username=username).exists():
            messages.error(request, 'This username is already taken')
            return redirect('register')

        # Check email
        if User.objects.filter(email=email).exists():
            messages.error(request, 'This email is already taken')
            return redirect('register')

        user = User.objects.create_user(
            username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()
        messages.success(request, 'You are now registered and can login.')
        return redirect('login')
    return render(request, 'accounts/register.html')


def dashboard(request):
    if request.method == 'POST':
        # dashboard
        return
    return render(request, 'accounts/dashboard.html')


def logout(request):
    if request.method == 'POST':
        # logout user
        auth.logout(request)
        messages.success(request, 'You are now loged out')
        return redirect('index')
    return redirect('index')
