from django.urls import path
from . import views
urlpatterns=[
    path('', views.index,name="index"),
    path('the-list/', views.the_list, name="list"),
    path('the-list/<slug:slug>', views.company_profile, name="company_profile"),
    path('the-list/<slug:slug>/review', views.create_review, name="create_review"),
    path('the-list/delete_review/<int:review_id>', views.delete_review, name="delete_review"),
    path('the-list/edit_review/<int:review_id>', views.edit_review, name="edit_review")
]