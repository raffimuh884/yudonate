from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Home

def home(request):
    return render(request, 'home.html')

# REGISTER

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username sudah digunakan')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Akun berhasil dibuat')
        return redirect('login')

    return render(request, 'register.html')

# LOGIN

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Login gagal')
            return redirect('login')

    return render(request, 'login.html')

# LOGOUT

def logout_view(request):
    logout(request)
    return redirect('login')

def donate(request):
    return render(request, 'donate.html')

def campaign(request):
    return render(request, 'campaign.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def donatehistory(request):
    return render(request, 'donatehistory.html')
def formdonate(request):
    return render(request, 'formdonate.html')
