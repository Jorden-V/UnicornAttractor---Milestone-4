from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Bug
from .forms import CreateBugForm

# Create your views here.

def view_bugs(request):
    bugs = Bug.objects.all().order_by('-id')
    return render(request, "bugs.html", {"bugs": bugs})
    
def bug_detail(request, pk):
    """
    Create a view that returns a single
    bug object based on the bug ID (pk) and
    render it to the bug_detail.html template
    or return 404 error if object is not found
    """
    bug = get_object_or_404(Bug, pk=pk)
    return render(request, 'bug_detail.html', {'bug':bug})
