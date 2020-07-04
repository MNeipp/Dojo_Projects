from django.shortcuts import render, redirect
from login_app.models import User

# Create your views here.

def index(request):
    if "user_id" in request.session:
        context={
            "logged_user": User.objects.get(id=request.session['user_id']),
        }
        return render(request, "index.html", context)
    else:
        return render(request, "index.html")

def shop(request):
    if "user_id" in request.session:
        context={
            "logged_user": User.objects.get(id=request.session['user_id'])
        }
        return render(request, "shop.html", context)
    else:
        return render(request, "shop.html")

def product_info(request, product_id):
    if "user_id" in request.session:
        context={
            "logged_user": User.objects.get(id=request.session['user_id'])
        }
        return render(request, "product_info.html", context)
    else:
        return render(request, "product_info.html")

def cart(request):
    return render(request, "cart.html")