from django.shortcuts import render, redirect, HttpResponse, reverse
from user_app.models import User
from .models import Company, Review, Report
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

def the_list_filtered(request):
    company_list = Company.objects.all()
    context={
        'companies': CompanyFilter(request.GET, queryset=company_list)
    }
    return render(request, "snippets/list_filtered.html", context)

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

def create_review(request, slug):
    if int(request.POST['rating']) < 1  or int(request.POST['rating']) > 5:
        messages.error(request, "Please enter a valid rating")
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    company = Company.objects.get(slug=slug)
    logged_user = User.objects.get(id=request.session['user_id'])
    if "anonymous" in request.POST:
        new_review = Review.objects.create(content = request.POST['content'], rating = request.POST['rating'], creator = logged_user, company = company)
    else:
        new_review = Review.objects.create(content = request.POST['content'], rating = request.POST['rating'], creator = logged_user, company = company, anonymous=False)
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def delete_review(request, review_id):
    if request.method == "POST":
        to_delete = Review.objects.get(id=review_id)
        to_delete.delete()
        context={
        "logged_user":User.objects.get(id=request.session['user_id'])
        }
        return render (request, "snippets/user_reviews_snippet.html", context)
    else:
        return redirect(reverse('index'))

def edit_review(request, review_id):
    if request.method == "POST":
        if int(request.POST['rating']) < 1  or int(request.POST['rating']) > 5:
            return HttpResponse("<h3 class='text-danger'> Please enter a valid rating </h3>")
        to_edit = Review.objects.get(id=review_id)
        to_edit.rating = request.POST['rating']
        to_edit.content = request.POST['content']
        to_edit.save()
        context={
            "logged_user":User.objects.get(id=request.session['user_id'])
        }
        return render (request, "snippets/user_reviews_snippet.html", context)
    else:
        return redirect(reverse('index'))

def privacy_policy(request):
    if 'user_id' not in request.session:
        return render(request, "privacy_policy.html")
    else:
        context={
            'logged_user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, "privacy_policy.html", context)


def terms_of_use(request):
    if 'user_id' not in request.session:
        return render(request, "terms_of_use.html")
    else:
        context={
            'logged_user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, "terms_of_use.html", context)

def about(request):
    if 'user_id' not in request.session:
        return render(request, "about.html")
    else:
        context={
            'logged_user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, "about.html", context)

def report(request, review_id):
    if request.method == "POST":
        review = Review.objects.get(id=review_id)
        reporter = User.objects.get(id=request.POST['reporter_id'])
        Report.objects.create(content = request.POST['content'], review=review, reporter = reporter)
        return HttpResponse("<h2>Thank you for your report!</h2>")
    
    else:
        if 'user_id' not in request.session:
            return render(request, "report.html") 
        else:
            context={
            'logged_user': User.objects.get(id=request.session['user_id']),
            'review': Review.objects.get(id=review_id)
        }
        return render(request, "report.html", context)

def contribute(request):
    if request.method == "POST":
        pass
    else:
        if 'user_id' not in request.session:
            return render(request, "report.html") 
        else:
            context={
            'logged_user': User.objects.get(id=request.session['user_id']),
        }
        return render(request, "report.html", context)