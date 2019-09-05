from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from bugs.models import Bug
from features.models import Feature
from forum.models import ForumPost


def do_search(request):
    """View that returns keyword searchs and renders search html with the results"""
    bugs = Bug.objects.filter(
        name__icontains=request.GET['q']).exclude(
        status='Cancelled').exclude(
            status="Done")
    features = Feature.objects.filter(
        name__icontains=request.GET['q']).exclude(
        status='Cancelled').exclude(
            status="Done")
    posts = ForumPost.objects.filter(name__icontains=request.GET['q'])
    bugs = bugs.order_by("-upvotes")
    features = features.order_by("-upvotes")
    posts = posts.order_by("-upvotes")
    total = bugs.count() + features.count() + posts.count()
    return render(request,
                  "search.html",
                  {"bugs": bugs,
                   "features": features,
                   "posts": posts,
                   "total": total})
