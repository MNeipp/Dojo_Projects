from django.urls import path
from . import views
urlpatterns=[
    path('', views.index,name="index"),
    path('the-list/', views.the_list, name="list"),
    path('the-list/<slug:slug>', views.company_profile, name="company_profile"),
    path('profile', views.user_profile, name="user_profile"),
    path('profile/update', views.update_profile, name="update_user_profile"),
    path('profile/update_password', views.update_password, name="update_password")
]