from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ForumPost, ForumComment, ForumPostUpvote
from .forms import ForumPostForm, ForumCommentForm

def view_posts(request):
    posts = ForumPost.objects.all()
    return render(request, "forum.html", {"posts": posts})

def post_detail(request, pk):
    """
    Create a view that returns a single
    post object based on the post ID (pk) and
    render it to the post_detail.html template
    or return 404 error if object is not found
    """
    post = get_object_or_404(ForumPost, pk=pk)
    if request.method == "POST":
        
        form = ForumCommentForm(request.POST)
        
        if form.is_valid():
            postComment = form.save(commit=False)
            postComment.post = post
            postComment.author = request.user
            post.comment_number += 1
            post.save()
            postComment.save()
            return redirect(reverse('post_detail', kwargs={'pk': pk}))
            
    else:
        form = ForumCommentForm()
        comments = ForumComment.objects.filter(post__pk=post.pk)
        comments_total = len(comments)
        post.views += 1
        post.save()
        return render(request, 'post_detail.html', {'post':post, 'comments':comments, 'comments_total':comments_total, 'form':form})

@login_required()        
def upvote_post(request, pk):
    """
    Stops user voting multiple times if they have already.
    """
    post = ForumPost.objects.get(pk=pk)
    if ForumPostUpvote.objects.filter(user=request.user, post=post):
        messages.error(request, "You have upvoted this post already!", extra_tags="alert-danger")
    else:
        post.upvotes += 1
        post.save()
        ForumPostUpvote.objects.create(user=request.user, post=post)
        messages.success(request, "Your vote has been accepted!", extra_tags="alert-success")
    return redirect('view_posts')
    
@login_required()        
def add_or_edit_post(request, pk=None):
    """
    Create a view that allows us to create or edit a post
    depending if the PostID is null or not
    """
    post =  get_object_or_404(ForumPost, pk=pk) if pk else None
    
    if request.method == "POST":
        form = ForumPostForm(request.POST, instance=post)
        
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(post_detail, post.pk)
            
    else:
        form = ForumPostForm(instance=post)
    return render(request, 'create_post.html', {'form':form})

@login_required()    
def delete_post(request, pk):
     post =  get_object_or_404(ForumPost, pk=pk) 
     post.delete()
     return redirect('profile')