from django.shortcuts import render, redirect


def login(request):
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        # register user
        return
    return render(request, 'accounts/register.html')


def dashboard(request):
    if request.method == 'POST':
        # register user
        return
    return render(request, 'accounts/dashboard.html')


def logout(request):
    if request.method == 'POST':
        # register user
        return
    return redirect('index')
