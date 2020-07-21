from django.contrib import admin
from vocalist_app.models import Company, Review, Report, YAPRequest, Correction
from user_app.models import User

# Register your models here.
admin.site.register(User)
admin.site.register(Company)
admin.site.register(Review)
admin.site.register(Report)
admin.site.register(YAPRequest)
admin.site.register(Correction)
