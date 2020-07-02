from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, "index.html")

def shop(request):
    return render(request, "shop.html")

def product_info(request, product_id):
    return render(request, "product_info.html")

def cart(request):
    return render(request, "cart.html")