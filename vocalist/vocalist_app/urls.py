from django.urls import path
from . import views
urlpatterns=[
    path('', views.index,name="index"),
    path('the-list/', views.the_list, name="list"),
]