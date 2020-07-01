from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, "index.html")

def shop(request):
    return render(request, "shop.html")