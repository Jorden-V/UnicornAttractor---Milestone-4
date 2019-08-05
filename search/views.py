from django.shortcuts import render
from django.contrib import messages
from bugs.models import Bug
from features.models import Feature

# Create your views here.
def do_search(request):
    bugs = Bug.objects.filter(name__icontains=request.GET['q'])
    features = Feature.objects.filter(name__icontains=request.GET['q'])
    if not bugs:
        messages.error(request, "Unfortunately your search didn't find anything")
    elif not features:
        messages.error(request, "Unfortunately your search didn't find anything")
    else: 
        bugs = bugs.order_by("-upvotes")
        features = features.order_by("-upvotes")
    return render(request, "search.html", {"bugs": bugs, "features": features})
