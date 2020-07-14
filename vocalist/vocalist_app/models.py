from django.db import models
from user_app.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify


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

class Review(models.Model):
    content = models.TextField(blank= True, null=True)
    rating = models.IntegerField()
    company = models.ForeignKey(Company, related_name = "has_reviews", on_delete=models.CASCADE)
    creator = models.ForeignKey(User, related_name="has_reviewed", on_delete=models.CASCADE)
    anonymous = models.BooleanField(default = True)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now= True)
