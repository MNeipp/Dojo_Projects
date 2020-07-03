from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.

def login(request):
    return render(request, "login.html")

def registration(request):
    return render(request, "registration.html")

def create_user(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value, extra_tags=key)
            return (reverse("login"))
        else:
            first_name = request.POST['first_name']
            last_name=request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            pswd_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(first_name=first_name, last_name = last_name, email=email, password=pswd_hash)
            if "user_id" not in request.session:
                request.session['user_id'] = user.id
            return redirect (reverse("home"))