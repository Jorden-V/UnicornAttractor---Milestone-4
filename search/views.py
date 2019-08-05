from django.shortcuts import render
from bugs.models import Bug
from features.models import Feature

# Create your views here.
def do_search(request):
    bugs = Bug.objects.filter(name__icontains=request.GET['q'])
    features = Feature.objects.filter(name__icontains=request.GET['q'])
    return render(request, "search.html", {"bugs": bugs, "features": features})
