from django.shortcuts import render, redirect, reverse, get_object_or_404
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
            featureComment.save()
            return redirect(reverse('feature_detail', kwargs={'pk': pk}))
            
    else:
        form = FeatureCommentForm()
        comments = FeatureComment.objects.filter(feature__pk=feature.pk)
        comments_total = len(comments)
        feature.views += 1
        feature.save()
        return render(request, 'feature_detail.html', {'feature':feature, 'comments':comments, 'comments_total':comments_total, 'form':form})
        

def add_or_edit_feature(request, pk=None):
    """
    Create a view that allows us to create or edit a bug
    depending if the PostID is null or not
    """
    feature =  get_object_or_404(Feature, pk=pk) if pk else None
    
    if request.method == "POST":
        form = CreateFeatureForm(request.POST, instance=feature)
        
        
        if form.is_valid():
            feature = form.save(commit=False)
            feature.author = request.user
            feature.save()
            return redirect(feature_detail, feature.pk)
            
    else:
        form = CreateFeatureForm(instance=feature)
    return render(request, 'create_feature.html', {'form':form})


def delete_feature(request, pk):
     feature =  get_object_or_404(Feature, pk=pk) 
     feature.delete()
     return redirect('profile')