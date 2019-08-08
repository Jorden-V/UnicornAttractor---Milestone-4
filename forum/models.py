from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class ForumPost(models.Model):
    name = models.CharField(max_length=75, blank=False)
    desc = models.TextField(max_length=500, blank=False)
    author = models.ForeignKey(User, related_name='posted_by')
    views = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        
class ForumComment(models.Model):
    description = models.TextField(max_length=256, blank=False)
    post = models.ForeignKey(ForumPost)
    author = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.description