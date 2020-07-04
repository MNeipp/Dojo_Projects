from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.

def login(request):
    return render(request, "login.html")

def login_process(request):
    if request.method=="POST":
        if len(request.POST['email']) < 5:
            messages.error(request, "Please enter a valid e-mail", extra_tags="email")
            return redirect(reverse('login'))
        user = User.objects.filter(email__iexact=request.POST['email'])
        request.session['email'] = request.POST['email']
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                return redirect(reverse('home'))
            else:
                messages.error(request,"Incorrect password", extra_tags="password")
                return redirect(reverse('login'))
        else:
            messages.error(request, "E-mail not registered", extra_tags="email")
            return redirect (reverse('login'))

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

def logout(request):
    request.session.flush()
    return redirect (reverse("home"))