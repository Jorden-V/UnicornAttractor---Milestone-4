from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Bug, BugComment, BugUpvote
from .forms import CreateBugForm, BugCommentForm

# Create your views here.
@login_required()
def view_bugs(request):
    bugs = Bug.objects.all().order_by('-id')
    return render(request, "bugs.html", {"bugs": bugs})
    
@login_required()
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

@login_required()
def upvote_bug(request, pk):
    """
    Stops user voting multiple times if they have already.
    """
    bug = Bug.objects.get(pk=pk)
    if BugUpvote.objects.filter(user=request.user, bug=bug):
        messages.error(request, "You have upvoted this bug already!")
    else:
        bug.upvotes += 1
        bug.save()
        BugUpvote.objects.create(user=request.user, bug=bug)
        messages.error(request, "Your vote has been accepted!")
    return redirect('view_bugs')


def add_or_edit_bug(request, pk=None):
    """
    Create a view that allows us to create or edit a bug
    depending if the PostID is null or not
    """
    bug =  get_object_or_404(Bug, pk=pk) if pk else None
    
    if request.method == "POST":
        form = CreateBugForm(request.POST, instance=bug)
        
        
        if form.is_valid():
            bug = form.save(commit=False)
            bug.author = request.user
            bug.save()
            return redirect(bug_detail, bug.pk)
            
    else:
        form = CreateBugForm(instance=bug)
    return render(request, 'create_bug.html', {'form':form})


def delete_bug(request, pk):
     bug =  get_object_or_404(Bug, pk=pk) 
     bug.delete()
     return redirect('profile')