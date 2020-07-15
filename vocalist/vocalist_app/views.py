from django.shortcuts import render, redirect, HttpResponse, reverse
from user_app.models import User
from .models import Company, Review
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
    if 'user_id' not in request.session:
        return render(request, "list.html")
    else:
        context={
            'logged_user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, "list.html", context)
        

def company_profile(request, slug):
    if 'user_id' not in request.session:
        return render(request, "company_profile.html")
    else:
        context={
            'company': Company.objects.get(slug=slug),
            'logged_user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, "company_profile.html", context)
 

def user_profile(request):
    if 'user_id' not in request.session:
        return reverse('login')
    context={
        'logged_user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, "user_profile.html", context)

def update_profile(request):
    if request.method == "GET":
        return redirect(reverse('index'))
    errors = User.objects.info_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value, extra_tags=key)
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    logged_user = User.objects.get(id=request.session['user_id'])
    logged_user.first_name = request.POST['first_name']
    logged_user.last_name = request.POST['last_name']
    logged_user.email = request.POST['email']
    if 'anonymous' in request.POST:
        logged_user.anonymous = True
    else:
        logged_user.anonymous = False
    if 'profile_picture' in request.FILES:
        logged_user.image = request.FILES['profile_picture']
    logged_user.save()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def update_password(request):
    if request.method == "GET":
        return redirect(reverse('index'))
    logged_user = User.objects.get(id=request.session['user_id'])
    if bcrypt.checkpw(request.POST['current_password'].encode(), logged_user.password.encode()):
        if len(request.POST['new_password']) < 8:
            messages.error(request,"Password must be at least 8 characters long", extra_tags="confirm")
            return redirect(reverse('user_profile'))
        elif request.POST['new_password'] != request.POST['confirm_password']:
            messages.error(request, "Passwords don't match", extra_tags="confirm")
            return redirect(reverse('user_profile'))       
        else:
            password = request.POST['new_password']
            pswd_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            logged_user.password = pswd_hash
            logged_user.save()
            return redirect(reverse('user_profile'))
    else:
        messages.error(request,"Incorrect password", extra_tags="password")
        return redirect(reverse('user_profile'))
    

