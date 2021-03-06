from django.db import models
from user_app.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from datetime import datetime


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)
    weekly_stipend = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.CharField(max_length=20)
    agma = models.BooleanField(default = False)
    housing = models.BooleanField(default = False)
    travel_stipend = models.BooleanField(default=False)
    benefits = models.BooleanField(default=False)
    slug = models.SlugField(unique= True, max_length=255, null=True, blank=True)
    description = models.TextField(blank = True, null = True)
    website = models.URLField(blank = True, null = True)
    logo = models.TextField(blank=True, null=True)
    minimum_age = models.IntegerField(blank=True, null=True)
    maximum_age = models.IntegerField(blank=True, null =True)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now= True)


    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def averageRating(self):
        if self.has_reviews.all():
            num = 0
            for review in self.has_reviews.all():
                num += review.rating
            return round((num/self.has_reviews.all().count()),2)
        else:
            return "no reviews"

class Review(models.Model):
    content = models.TextField(blank= True, null=True)
    rating = models.IntegerField()
    company = models.ForeignKey(Company, related_name = "has_reviews", on_delete=models.CASCADE)
    creator = models.ForeignKey(User, related_name="has_reviewed", on_delete=models.CASCADE)
    anonymous = models.BooleanField(default = True)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now= True)

    def datePosted(self):
        return datetime.strftime(self.created_at, "%B %d, %Y")
    
    def dateEdited(self):
        return datetime.strftime(self.updated_at, "%B %d, %Y")

class Report(models.Model):
    content = models.TextField()
    review = models.ForeignKey(Review, related_name = "has_reports", on_delete=models.CASCADE)
    reporter = models.ForeignKey(User, related_name="has_reported", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now= True)

class YAPRequest(models.Model):
    name = models.CharField(max_length=255)
    weekly_stipend = models.CharField( max_length = 50, blank=True, null=True)
    category = models.CharField(max_length=20)
    agma = models.BooleanField(default = False)
    housing = models.BooleanField(default = False)
    travel_stipend = models.BooleanField(default=False)
    benefits = models.BooleanField(default=False)
    minimum_age = models.CharField(max_length = 3, blank=True, null=True)
    maximum_age = models.CharField(max_length = 3, blank=True, null =True)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now= True)

class Correction(models.Model):
    content = models.TextField()
    company = models.ForeignKey(Company, related_name = "has_corrections", on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, related_name="has_corrected", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now= True)
