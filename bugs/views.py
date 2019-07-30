from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Bug, BugComment
from .forms import CreateBugForm, BugCommentForm

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
    if request.method == "POST":
        
        form = BugCommentForm(request.POST)
        
        if form.is_valid():
            bugComment = form.save(commit=False)
            bugComment.bug = bug
            bugComment.author = request.user
            bugComment.save()
            return redirect(reverse('bug_detail', kwargs={'pk': pk}))
            
    else:
        form = BugCommentForm()
        comments = BugComment.objects.filter(bug__pk=bug.pk)
        comments_total = len(comments)
        bug.views += 1
        bug.save()
        return render(request, 'bug_detail.html', {'bug':bug, 'comments':comments, 'comments_total':comments_total, 'form':form})


def upvote_bug(request, pk):
    """
    A view that upvotes the selected bug
    """
    if request.method == "POST":
        bug = get_object_or_404(Bug, pk=pk)
        bug.upvotes += 1
        bug.save()
        return redirect('view_bugs')