from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from bugs.models import Bug
from features.models import Feature
from forum.models import ForumPost

# Create your views here.
@login_required()
def do_search(request):
    bugs = Bug.objects.filter(name__icontains=request.GET['q'])
    features = Feature.objects.filter(name__icontains=request.GET['q'])
    posts = ForumPost.objects.filter(name__icontains=request.GET['q'])
    bugs = bugs.order_by("-upvotes")
    features = features.order_by("-upvotes")
    posts = posts.order_by("-upvotes")
    return render(request, "search.html", {"bugs": bugs, "features": features, "posts": posts})
