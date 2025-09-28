from django.shortcuts import render, redirect
from .models import *
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm


# Create your views here.
# Home page
def index(request):
    return render(request, 'index.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        first_name = request.POST.get('Firstname')
        last_name = request.POST.get('Lastname')
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        user = CustomUser.objects.create_user(
            username = email, 
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        login(request, user)
        return render(request, 'home.html')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'home.html')