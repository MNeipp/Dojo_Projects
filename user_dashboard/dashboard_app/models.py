from django.db import models
from login_app.models import User
from django.utils import timezone
import math


# Create your models here.
class Post(models.Model):
    content = models.TextField()
    board = models.ForeignKey(User, related_name="board_posts", on_delete=models.CASCADE)
    creator = models.ForeignKey(User, related_name="has_posts", on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="liked_posts")
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def canDelete(self):
        now = timezone.now()
        diff = now - self.created_at

        if diff.days >= 0 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)
            if minutes <= 15:
                return True
            else: 
                return False
        else:
            return False

    def whenCreated(self):
        now = timezone.now()
        diff = now - self.created_at

        # seconds/minutes/hours
        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            if seconds == 1:
                return str(seconds) +  " second ago"
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)
            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)
            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"

        # months
        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"

        #  years
        if diff.days >= 365:
            years= math.floor(diff.days/365)
            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"

    def numberOfLikes(self):
        likes = self.likes.all()
        if len(likes) == 1:
            return str(len(likes)) + " person likes this"
        else:
            return str(len(likes)) + " people like this"

class Comment(models.Model):
    content = models.TextField()
    creator = models.ForeignKey(User, related_name="has_comments", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="has_comments", on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="liked_comments")
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def canDelete(self):
        now = timezone.now()
        diff = now - self.created_at

        if diff.days >= 0 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)
            if minutes <= 15:
                return True
            else: 
                return False
        else:
            return False

    def whenCreated(self):
        now = timezone.now()
        diff= now - self.created_at
        
        # seconds/minutes/hours
        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            if seconds == 1:
                return str(seconds) +  " second ago"
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)
            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)
            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"

        # months
        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"

        #  years
        if diff.days >= 365:
            years= math.floor(diff.days/365)
            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"

    def numberOfLikes(self):
        likes = self.likes.all()
        if len(likes) == 1:
            return str(len(likes)) + " person likes this"
        else:
            return str(len(likes)) + " people like this"
