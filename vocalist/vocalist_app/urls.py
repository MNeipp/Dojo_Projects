from django.urls import path
from . import views
urlpatterns=[
    path('', views.index,name="index"),
    path('the-list/', views.the_list, name="list"),
    path('the-list/<slug:slug>', views.company_profile, name="company_profile"),
    path('the-list/<slug:slug>/review', views.leave_review, name="leave_review"),
]