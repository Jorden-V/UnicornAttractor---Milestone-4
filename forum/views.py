from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import ForumPost, ForumComment
from .forms import ForumPostForm, ForumCommentForm

def view_posts(request):
    posts = ForumPost.objects.all()
    return render(request, "forum.html", {"posts": posts})