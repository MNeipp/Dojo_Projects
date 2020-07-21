from django.shortcuts import render, redirect, HttpResponse, reverse
from user_app.models import User
from .models import Company, Review, Report, YAPRequest, Correction
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
            'companies': CompanyFilter(request.GET, queryset=company_list)
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

def report_correction(request, slug):
    if request.method == "POST":
        user = User.objects.get(id=request.session['user_id'])
        company = Company.objects.get(slug=slug)
        Correction.objects.create(user = user, company = company, content = request.POST['content'])
        return HttpResponse("<h2>Thank you for the information!</h2>")
    else:
        if 'user_id' not in request.session:
            context={
                "company": Company.objects.get(slug=slug)
            }
        else:
            context={
                'company': Company.objects.get(slug=slug),
                'logged_user': User.objects.get(id=request.session['user_id'])
            }
        return render(request, 'correction.html', context)


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

def all_reports(request):
    if 'user_id' not in request.session:
        return redirect(reverse('index'))
    user = User.objects.get(id=request.session['user_id'])
    if user.user_level != 9:
        return redirect(reverse('index'))
    else:
        context={
            'logged_user': user,
            'reports': Report.objects.all()
        }
        return render(request, 'all_reports.html', context)

def delete_report(request, report_id):
    if 'user_id' not in request.session:
        return redirect(reverse('index'))
    user = User.objects.get(id=request.session['user_id'])
    if user.user_level != 9:
        return redirect(reverse('index'))
    else:
        to_delete = Report.objects.get(id=report_id)
        to_delete.delete()
        return redirect(reverse('all_reports'))

def contribute(request):
    if request.method == "POST":
        name = request.POST['name']
        category = request.POST['category']
        weekly_stipend = request.POST['weekly_stipend']
        if 'agma' in request.POST:
            agma = True
        else:
            agma = False
        if 'benefits' in request.POST:
            benefits = True
        else:
            benefits = False
        if 'housing' in request.POST:
            housing = True
        else:
            housing = False
        if 'travel_stipend' in request.POST:
            travel_stipend = True
        else:
            travel_stipend = False
        min_age = request.POST['min_age']
        max_age = request.POST['max_age']
        
        YAPRequest.objects.create(name = name, weekly_stipend = weekly_stipend, category = category, agma = agma, housing = housing, benefits = benefits, travel_stipend = travel_stipend, maximum_age= max_age, minimum_age = min_age)
        return HttpResponse("<h2>Thank you for contributing!</h2>")
    else:
        if 'user_id' not in request.session:
            return render(request, "contribute.html") 
        else:
            context={
            'logged_user': User.objects.get(id=request.session['user_id']),
        }
        return render(request, "contribute.html", context)

def yap_requests(request):
    if 'user_id' not in request.session:
        return redirect(reverse('index'))
    user = User.objects.get(id=request.session['user_id'])
    if user.user_level != 9:
        return redirect(reverse('index'))
    else:
        context={
            'logged_user': user,
            'requests': YAPRequest.objects.all()
        }
        return render(request, 'YAP_requests.html', context)

def delete_request(request, request_id):
    if 'user_id' not in request.session:
        return redirect(reverse('index'))
    user = User.objects.get(id=request.session['user_id'])
    if user.user_level != 9:
        return redirect(reverse('index'))
    else:
        to_delete = YAPRequest.objects.get(id=request_id)
        to_delete.delete()
        return redirect(reverse('requests'))

def add_yap(request, request_id):
    if request.method == "POST":
        name = request.POST['name']
        weekly_stipend = request.POST['weekly_stipend']
        category = request.POST['category']
        description = request.POST['description']
        website = request.POST['website']
        logo = request.POST['logo']
        if 'agma' in request.POST:
            agma = True
        else:
            agma = False
        if 'travel_stipend' in request.POST:
            travel_stipend = True
        else:
            travel_stipend = False
        if 'benefits' in request.POST:
            benefits = True
        else:
            benefits = False
        if 'housing' in request.POST:
            housing = True
        else:
            housing = False
        if request.POST['min_age'] == 'None':
            min_age = -1
        else:
            min_age = request.POST['min_age']
        if request.POST['max_age'] == 'None':
            max_age = -1
        else:
            max_age = request.POST['max_age']
        website = request.POST['website']
        logo = request.POST['logo']
        
        Company.objects.create(name=name, weekly_stipend=weekly_stipend, category=category, agma=agma, housing=housing, travel_stipend=travel_stipend, benefits=benefits, description=description, website=website, logo=logo, minimum_age=min_age, maximum_age=max_age)
        filled_request = YAPRequest.objects.get(id=request_id)
        filled_request.delete()
        return redirect(reverse('requests'))

    if 'user_id' not in request.session:
        return redirect(reverse('index'))
    user = User.objects.get(id=request.session['user_id'])
    if user.user_level != 9:
        return redirect(reverse('index'))
    else:
        context={
            'logged_user':user,
            'request': YAPRequest.objects.get(id=request_id)
        }
        return render(request, 'add_yap.html', context)

def thank_you(request):
    if 'user_id' not in request.session:
        return render(request, "thank_you.html")
    else:
        context={
            'logged_user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, "thank_you.html", context)

def all_corrections(request):
    if 'user_id' not in request.session:
        return redirect(reverse('index'))
    user = User.objects.get(id=request.session['user_id'])
    if user.user_level != 9:
        return redirect(reverse('index'))
    else:
        context={
            'logged_user': user,
            'corrections': Correction.objects.all()
        }
        return render(request, 'all_corrections.html', context)

def update_yap(request, slug, correction_id):
    if request.method == "POST":
        name = request.POST['name']
        weekly_stipend = request.POST['weekly_stipend']
        category = request.POST['category']
        if 'agma' in request.POST:
            agma = True
        else:
            agma = False
        if 'travel_stipend' in request.POST:
            travel_stipend = True
        else:
            travel_stipend = False
        if 'benefits' in request.POST:
            benefits = True
        else:
            benefits = False
        if 'housing' in request.POST:
            housing = True
        else:
            housing = False
        if request.POST['min_age'] == 'None':
            min_age = -1
        else:
            min_age = request.POST['min_age']
        if request.POST['max_age'] == 'None':
            max_age = -1
        else:
            max_age = request.POST['max_age']
        
        to_correct = Company.objects.filter(slug=slug).update(name=name, weekly_stipend=weekly_stipend, category=category, agma=agma, housing=housing, travel_stipend=travel_stipend, benefits=benefits, minimum_age=min_age, maximum_age=max_age)
        filled_correction = Correction.objects.get(id=request.POST['correction_id'])
        filled_correction.delete()
        return redirect(reverse('all_corrections'))

    if 'user_id' not in request.session:
        return redirect(reverse('index'))
    user = User.objects.get(id=request.session['user_id'])
    if user.user_level != 9:
        return redirect(reverse('index'))
    else:
        context={
            'logged_user':user,
            'company': Company.objects.get(slug=slug),
            'correction': Correction.objects.get(id=correction_id),
        }
        return render(request, 'update_yap.html', context)

def delete_correction(request, correction_id):
    if 'user_id' not in request.session:
        return redirect(reverse('index'))
    user = User.objects.get(id=request.session['user_id'])
    if user.user_level != 9:
        return redirect(reverse('index'))
    else:
        to_delete = Correction.objects.get(id=correction_id)
        to_delete.delete()
        return redirect(reverse('all_corrections'))