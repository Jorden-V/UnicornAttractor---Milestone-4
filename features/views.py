from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Feature, FeatureComment
from .forms import CreateFeatureForm, FeatureCommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def view_features(request):
    """View to display all features excluding those with cancelled or done status"""
    features = Feature.objects.all().order_by('-id').exclude(status='Cancelled').exclude(status="Done")
    paginator = Paginator(features, 5)  # Show 5 features per page

    page = request.GET.get('page')
    try:
        features = paginator.page(page)
    except PageNotAnInteger:
        features = paginator.page(1)
    except EmptyPage:
        features = paginator.page(paginator.num_pages)
    return render(request, "features.html", {"features": features})


def view_completed_features(request):
    """View to display completed features"""
    features = Feature.objects.all().order_by('-id').filter(status='Done')
    paginator = Paginator(features, 5)  # Show 5 features per page

    page = request.GET.get('page')
    try:
        features = paginator.page(page)
    except PageNotAnInteger:
        features = paginator.page(1)
    except EmptyPage:
        features = paginator.page(paginator.num_pages)
    return render(request, "completed_features.html", {"features": features})


def feature_detail(request, pk):
    """
    Create a view that returns a single
    bug object based on the bug ID (pk) and
    render it to the bug_detail.html template
    or return 404 error if object is not found
    """
    feature = get_object_or_404(Feature, pk=pk)
    if request.method == "POST":

        form = FeatureCommentForm(request.POST)

        if form.is_valid():
            featureComment = form.save(commit=False)
            featureComment.feature = feature
            featureComment.author = request.user
            feature.comment_number += 1
            feature.save()
            featureComment.save()
            return redirect(reverse('feature_detail', kwargs={'pk': pk}))
        else:
            messages.error(
                    request,
                    "Looks like your comment is empty!",
                    extra_tags="alert-danger")
            form = FeatureCommentForm(instance=feature)
            return redirect(reverse('feature_detail', kwargs={'pk': pk}))

    else:
        form = FeatureCommentForm()
        comments = FeatureComment.objects.filter(feature__pk=feature.pk)
        comments_total = len(comments)
        feature.views += 1
        feature.save()
        return render(request,
                      'feature_detail.html',
                      {'feature': feature,
                       'comments': comments,
                       'comments_total': comments_total,
                       'form': form})


@login_required
def add_or_edit_feature(request, pk=None):
    """View to add or edit feature, if you are the feature creator"""
    feature = get_object_or_404(Feature, pk=pk) if pk else None
    if feature is not None:
        author = feature.author
        if author == request.user:
            if request.method == "POST":
                form = CreateFeatureForm(request.POST, instance=feature)

                if form.is_valid():
                    feature = form.save(commit=False)
                    feature.author = request.user
                    feature.save()
                    return redirect(feature_detail, feature.pk)
            else:
                form = CreateFeatureForm(instance=feature)
            return render(request, 'create_feature.html', {'form': form})
        else:
            messages.error(
                request,
                "This is not yours to edit!",
                extra_tags="alert-danger")
            return redirect(reverse('index'))
    else:
        if request.method == "POST":
            form = CreateFeatureForm(request.POST)
            if form.is_valid():
                feature = form.save(commit=False)
                feature.author = request.user
                feature.save()
                return redirect(reverse('view_features'))
        else:
            form = CreateFeatureForm()
        return render(request, 'create_feature.html', {'form': form})


@login_required()
def delete_feature(request, pk):
    """View to delete feature if user created it"""
    feature = get_object_or_404(Feature, pk=pk)
    author = feature.author
    if author == request.user:
        feature.delete()
    else:
        messages.error(
            request,
            "This is not yours to delete!",
            extra_tags="alert-danger")
        return redirect(reverse('index'))
    return redirect('profile')

@login_required
def delete_feature_comment(request, pk):
    comment = get_object_or_404(FeatureComment, pk=pk)
    feature = comment.feature
    if request.user == comment.author:
        comment.delete()
        messages.success(request, 'This comment has been deleted.')
    else:
        messages.info(request,
                      'You do not have permission to delete this comment.')
    return redirect('feature_detail', pk=feature.pk)