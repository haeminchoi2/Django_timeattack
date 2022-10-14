from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from user.models import MyUser

# Create your views here.
def signup_view(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        phone = request.POST['phone']
        address = request.POST['address']
        
        new_user = MyUser()
        new_user.username = username
        new_user.password = password
        new_user.phone = phone
        new_user.address = address
        
        new_user.set_password(password)
        new_user.save()
        return redirect('user:login')
    

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user=user)
            return redirect('user:home')
        else:
            return redirect('user:login')
        

def home_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'home.html')
        else:
            return redirect('user:login')
