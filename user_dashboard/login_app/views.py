from django.shortcuts import render, redirect, reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import User
import bcrypt, json


# Create your views here.
def signin(request):
    if 'email'in request.session:
        email = request.session['email']
    else:
        email=''
    context={
        "email": email,
    }
    return render(request,"signin.html", context)

def register(request):
    return render(request, "register.html")

@csrf_exempt
def ajax_process(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value, extra_tags=key)
        return render(request, "snippets/register_snippet.html")


def process(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value, extra_tags=key)
        if "user_id" in request.session:
            return redirect(reverse("new_user"))
        else:
            return redirect(reverse("register"))
    else:
        users = User.objects.all()
        if len(users) < 1:
            user_level = 9
        else:
            user_level = 0
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        pswd_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(first_name = first_name, last_name=last_name, email = email, password = pswd_hash, user_level = user_level)
        if "user_id" not in request.session:
            request.session['user_id'] = user.id
        return redirect(reverse('dashboard'))

def login(request):
    if len(request.POST['email']) < 1:
        messages.error(request, "Please enter a valid e-mail", extra_tags="email")
        return redirect(reverse('signin'))
    user = User.objects.filter(email__iexact=request.POST['email'])
    request.session['email'] = request.POST['email']
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect(reverse('dashboard'))
        else:
            messages.error(request,"Incorrect password", extra_tags="password")
            return redirect(reverse('signin'))
    else:
        messages.error(request, "E-mail not registered", extra_tags="email")
        return redirect (reverse('signin'))

def logout(request):
    request.session.flush()
    return redirect(reverse('home'))