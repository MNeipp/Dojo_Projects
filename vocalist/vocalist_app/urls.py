from django.urls import path
from . import views
urlpatterns=[
    path('', views.index,name="index"),
    path('the-list', views.the_list, name="list"),
    path('the-list/contribute', views.contribute, name="contribute"),
    path('the-list/about', views.about, name="about"),
    path('the-list/thank-you', views.thank_you, name="thank_you"),
    path('the-list/filtered', views.the_list_filtered, name="list_filtered"),
    path('the-list/<slug:slug>', views.company_profile, name="company_profile"),
    path('the-list/<slug:slug>/update/<int:correction_id>', views.update_yap, name="update_yap"),
    path('the-list/<slug:slug>/correction', views.report_correction, name="correction"),
    path('the-list/<slug:slug>/review', views.create_review, name="create_review"),
    path('the-list/delete_review/<int:review_id>', views.delete_review, name="delete_review"),
    path('the-list/edit_review/<int:review_id>', views.edit_review, name="edit_review"),
    path('privacy-policy', views.privacy_policy, name="privacy_policy"),
    path('terms-of-use', views.terms_of_use, name="terms_of_use"),
    path('the-list/report/<int:review_id>', views.report, name="report"),
    path('yap-requests', views.yap_requests, name="requests"),
    path('yap-requests/delete/<int:request_id>', views.delete_request, name="delete_request"),
    path('add-yap/<int:request_id>', views.add_yap, name="add_yap"),
    path('review-reports', views.all_reports, name="all_reports"),
    path('delete-report/<int:report_id>', views.delete_report, name="delete_report"),
    path('delete-correction/<int:correction_id>', views.delete_correction, name="delete_correction"),
    path('correction-reports', views.all_corrections, name="all_corrections"),
    
]