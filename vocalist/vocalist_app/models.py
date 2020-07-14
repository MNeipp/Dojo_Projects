from django.db import models
from user_app.models import User


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)
    weekly_stipend = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.CharField(max_length=20)
    agma = models.BooleanField()
    housing = models.BooleanField()
    description = models.TextField(blank = True, null = True)
    website = models.URLField(blank = True, null = True)
    logo = models.TextField(blank=True, null=True)
    minimum_age = models.IntegerField(blank=True, null=True)
    maximum_age = models.IntegerField(blank=True, null =True)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now= True)

    def __str__(self):
        return f'{self.name}'

class Review(models.Model):
    content = models.TextField(blank= True, null=True)
    rating = models.IntegerField()
    company = models.ManyToManyField(Company, related_name = "has_reviews")
    creator = models.ManyToManyField(User, related_name="has_reviewed")
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now= True)
