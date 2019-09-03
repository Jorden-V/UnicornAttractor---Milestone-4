from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ForumPost(models.Model):
    """Forum post model"""
    name = models.CharField(max_length=75, blank=False)
    description = models.TextField(max_length=500, blank=False)
    author = models.ForeignKey(User, related_name='posted_by')
    views = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    comment_number = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ForumComment(models.Model):
    """Forum post comment model"""
    comment = models.TextField(max_length=256, blank=False)
    post = models.ForeignKey(ForumPost)
    author = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class ForumPostUpvote(models.Model):
    """
    Model to upvote a bug
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title
