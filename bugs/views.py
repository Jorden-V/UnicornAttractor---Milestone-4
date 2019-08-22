from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Bug, BugComment, BugUpvote
from .forms import CreateBugForm, BugCommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def view_bugs(request):
    bugs = Bug.objects.all().order_by('-id').exclude(status='Cancelled').exclude(status="Done")
    paginator = Paginator(bugs, 5)  # Show 5 bugs per page

    page = request.GET.get('page')
    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)

    return render(request, "bugs.html", {"bugs": bugs})


def view_completed_bugs(request):
    bugs = Bug.objects.all().order_by('-id').filter(status='Done')

    paginator = Paginator(bugs, 5)  # Show 5 bugs per page

    page = request.GET.get('page')
    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)
    return render(request, "completed_bugs.html", {"bugs": bugs})


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
            bug.comment_number += 1
            bug.save()
            bugComment.save()
            return redirect(reverse('bug_detail', kwargs={'pk': pk}))

    else:
        form = BugCommentForm()
        comments = BugComment.objects.filter(bug__pk=bug.pk)
        comments_total = len(comments)
        bug.views += 1
        bug.save()
        return render(request,
                      'bug_detail.html',
                      {'bug': bug,
                       'comments': comments,
                       'comments_total': comments_total,
                       'form': form})


@login_required()
def upvote_bug(request, pk):
    """
    Stops user voting multiple times if they have already.
    """
    bug = Bug.objects.get(pk=pk)
    if BugUpvote.objects.filter(user=request.user, bug=bug):
        messages.error(
            request,
            "You have upvoted this bug already!",
            extra_tags="alert-danger")
    else:
        bug.upvotes += 1
        bug.save()
        BugUpvote.objects.create(user=request.user, bug=bug)
        messages.success(
            request,
            "Your vote has been accepted!",
            extra_tags="alert-success")
    return redirect('view_bugs')


@login_required
def add_or_edit_bug(request, pk=None):
    bug = get_object_or_404(Bug, pk=pk) if pk else None
    if bug is not None:
        author = bug.author
        if author == request.user:
            if request.method == "POST":
                form = CreateBugForm(request.POST, instance=bug)

                if form.is_valid():
                    bug = form.save(commit=False)
                    bug.author = request.user
                    bug.save()
                    return redirect(bug_detail, bug.pk)
            else:
                form = CreateBugForm(instance=bug)
            return render(request, 'create_bug.html', {'form': form})
        else:
            messages.error(
                request,
                "This is not yours to edit!",
                extra_tags="alert-danger")
            return redirect(reverse('index'))
    else:
        if request.method == "POST":
            form = CreateBugForm(request.POST)
            if form.is_valid():
                bug = form.save(commit=False)
                bug.author = request.user
                bug.save()
                return redirect(reverse('view_bugs'))
        else:
            form = CreateBugForm()
        return render(request, 'create_bug.html', {'form': form})


@login_required
def delete_bug(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    author = bug.author
    if author == request.user:
        bug.delete()
    else:
        messages.error(
            request,
            "This is not yours to delete!",
            extra_tags="alert-danger")
        return redirect(reverse('index'))
    return redirect('profile')
