from django.shortcuts import render, redirect, HttpResponse, reverse
from user_app.models import User
from .models import Company, Review
from .filters import CompanyFilter
from django.contrib import messages
import bcrypt


# Create your views here.

def index(request):
    if 'user_id' not in request.session:
        return render(request, "index.html")
    else:
        context={
            'logged_user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, "index.html", context)

def the_list(request):
    company_list = Company.objects.all()
    if 'user_id' in request.session:
        context={
            'companies': CompanyFilter(request.GET, queryset=company_list),
            'logged_user': User.objects.get(id=request.session['user_id'])
        }
    else:
        context={
            'companies': CompanyFilter(request.GET, queryset=company_list),
        }
    return render(request, "list.html", context)

def company_profile(request, slug):
    if 'user_id' not in request.session:
        context={
            'company': Company.objects.get(slug=slug),
        }
    else:
        context={
            'company': Company.objects.get(slug=slug),
            'logged_user': User.objects.get(id=request.session['user_id'])
        }
    return render(request, "company_profile.html", context)

def leave_review(request, slug):
    if request.method == "GET":
        return redirect(reverse("index"))
    else:
        company = Company.objects.get(slug=slug)
        logged_user = User.objects.get(id=request.session['user_id'])
        if "anonymous" in request.POST:
            new_review = Review.objects.create(content = request.POST['content'], rating = request.POST['rating'], creator = logged_user, company = company)
        else:
            new_review = Review.objects.create(content = request.POST['content'], rating = request.POST['rating'], creator = logged_user, company = company, anonymous=False)
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def ajax_review(request, slug):
    company = Company.objects.get(slug=slug)
    logged_user = User.objects.get(id=request.session['user_id'])
    if "anonymous" in request.POST:
        new_review = Review.objects.create(content = request.POST['content'], rating = request.POST['rating'], creator = logged_user, company = company)
    else:
        new_review = Review.objects.create(content = request.POST['content'], rating = request.POST['rating'], creator = logged_user, company = company, anonymous=False)
    context ={
        "review":new_review
    }
    return render(request, "snippets/review_snippet.html", context)

def delete_review(request, review_id):
    if request.method == "POST":
        to_delete = Review.objects.get(id=review_id)
        to_delete.delete()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def edit_review(request, review_id):
    pass

 


