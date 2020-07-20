from django.urls import path
from . import views
urlpatterns=[
    path('', views.index,name="index"),
    path('the-list/', views.the_list, name="list"),
    path('the-list/contribute', views.contribute, name="contribute"),
    path('the-list/about', views.about, name="about"),
    # path('the-list/donate', views.donate, name="donate"),
    path('the-list/filtered', views.the_list_filtered, name="list_filtered"),
    path('the-list/<slug:slug>', views.company_profile, name="company_profile"),
    path('the-list/<slug:slug>/review', views.create_review, name="create_review"),
    path('the-list/delete_review/<int:review_id>', views.delete_review, name="delete_review"),
    path('the-list/edit_review/<int:review_id>', views.edit_review, name="edit_review"),
    path('privacy-policy', views.privacy_policy, name="privacy_policy"),
    path('terms-of-use', views.terms_of_use, name="terms_of_use"),
    path('the-list/report/<int:review_id>', views.report, name="report"),
]