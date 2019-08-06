from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import ForumPost, ForumComment
from .forms import ForumPostForm, ForumCommentForm

def view_posts(request):
    posts = ForumPost.objects.all()
    return render(request, "forum.html", {"posts": posts})
    
def post_detail(request, pk):
    """
    Create a view that returns a single
    bug object based on the bug ID (pk) and
    render it to the bug_detail.html template
    or return 404 error if object is not found
    """
    post = get_object_or_404(ForumPost, pk=pk)
    if request.method == "POST":
        
        form = ForumCommentForm(request.POST)
        
        if form.is_valid():
            postComment = form.save(commit=False)
            postComment.post = post
            postComment.author = request.user
            postComment.save()
            return redirect(reverse('post_detail', kwargs={'pk': pk}))
            
    else:
        form = ForumCommentForm()
        comments = ForumComment.objects.filter(post__pk=post.pk)
        comments_total = len(comments)
        post.views += 1
        post.save()
        return render(request, 'post_detail.html', {'post':post, 'comments':comments, 'comments_total':comments_total, 'form':form})