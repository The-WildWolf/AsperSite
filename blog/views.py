from django.utils import timezone
from .models import Post, Comment
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .forms import PostForm, CommentForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    try:
        comments = get_list_or_404(Comment, post_id=pk)
    except:
        pass
    form = CommentForm(request.POST)

    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        content = form.cleaned_data['content']

        Comment.objects.create(
            name=name, email=email, content=content, post=post
        )
        return redirect('post_detail', pk=post.pk)
    try:
        return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})
    except UnboundLocalError:
        return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def search(request):
    query = request.GET['query']
    allPosts = Post.objects.filter(title__icontains=query)
    params = {'allPosts': allPosts}
    return render(request, 'blog/search.html', params)
