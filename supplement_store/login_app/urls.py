from django.urls import path
from . import views as login_views
from store_app import views as store_views

urlpatterns=[
    path('', login_views.login, name="login"),
    path('new', login_views.registration, name="registration"),


]