from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Bug
from .forms import CreateBugForm

# Create your views here.

def view_bugs(request):
    bugs = Bug.objects.all().order_by('-id')
    return render(request, "bugs.html", {"bugs": bugs})
