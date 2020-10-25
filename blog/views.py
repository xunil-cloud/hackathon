from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Post,Comment
from .forms import  CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def onecolumn(request):
    return render(request, 'blog/onecolumn.html')

def twocolumn1(request):
    return render(request, 'blog/twocolumn1.html')

def twocolumn2(request):
    return render(request, 'blog/twocolumn2.html')

def search(request):
    return redirect('post_list')
    #q = request.GET.get('q')

    #if not q:
    #    error_msg = "請輸入搜尋關鍵詞"
    #    messages.add_message(request, messages.ERROR, error_msg, extra_tags='danger')
    #    return redirect('blog:index')

    #post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    #return render(request, 'blog/index.html', {'post_list': post_list})
    
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            if (form.cleaned_data.get('comment_type') == 'P'):
                comment.post.number_of_positive_comments += 1
                comment.post.save()
            if (form.cleaned_data.get('comment_type') == 'N'):
                comment.post.number_of_negative_comments += 1
                comment.post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'form': form,'post': post})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
    