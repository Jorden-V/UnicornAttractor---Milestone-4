from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Feature, FeatureComment
from .forms import CreateFeatureForm, FeatureCommentForm

# Create your views here.
def view_features(request):
    features = Feature.objects.all().order_by('-id')
    return render(request, "features.html", {"features": features})

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
        form = FeatureCommentForm()
        comments = FeatureComment.objects.filter(feature__pk=feature.pk)
        comments_total = len(comments)
        feature.views += 1
        feature.save()
        return render(request, 'feature_detail.html', {'feature':feature, 'comments':comments, 'comments_total':comments_total, 'form':form})
        
@login_required

def add_or_edit_feature(request, pk=None):
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
            messages.error(request, "This is not yours to edit!", extra_tags="alert-danger")
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
    feature =  get_object_or_404(Feature, pk=pk)
    author = feature.author
    if author == request.user:
        feature.delete()
    else:
        messages.error(request, "This is not yours to delete!", extra_tags="alert-danger")
        return redirect(reverse('index'))
    return redirect('profile')
