from django.shortcuts import render, redirect, HttpResponse, reverse

# Create your views here.

def index(request):
    return render(request, "index.html")

def the_list(request):
    return render(request, "list.html")

def company_profile(request):
    return render(request, "company_profile.html")