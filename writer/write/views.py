from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import User
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'write/login.html')
    return render(request, 'write/index.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'write/index.html')
        else:
            return render(request, 'write/login.html', {'error': 'Invalid username or password'})
    return render(request, 'write/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'write/logout.html')

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "write/register.html", {
                "message": "Passwords must match"
            })
            
        try: 
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "write/register.html", {
                "message": "Username already taken"
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    return render(request, "write/register.html")