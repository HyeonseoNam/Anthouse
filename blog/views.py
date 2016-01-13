from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm, PostForm, TimelineForm
from django.contrib.auth.decorators import login_required



def test(request):
    post_list = Post.objects.all().order_by('-created_at')
    if request.method == 'POST':
        form = TimelineForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', post.pk)
    else:
        form = TimelineForm()
    return render(request, 'blog/test.html', {
        'post_list': post_list,
        'form':form,
    })

def chart(request):
    return render(request, 'blog/chart.html', {
    })


def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {
        'post_list': post_list,
    })

def post_detail(request, pk):
    post= Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post':post,
    })
@login_required
def post_create(request):

    #request.GET
    #request.POST
    #request.FILES

    #request.user =>
    # django.contrib.auth.models.AnonymousUser 로그인 안됐을때 자동 할당
    # django.contrib.auth.models.User  로그인 됐을때 자동 할당
    #


    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_forms.html',{
        'form':form,
    })

@login_required
def post_update(request,pk):
    post = Post.objects.get(pk=pk)

# 자기가 작성한 유저가 아니라 다른 유저가 로그인하면 수정 , 삭제 안되게 막는 2줄 코드 -> 포스트 디테일로 돌아오게 만듬
    if post.author != request.user:
        return redirect('blog:post_detail', pk)

    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('blog:post_detail', post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_forms.html',{
        'form':form,
    })

@login_required
def post_delete(request, pk):
    post =Post.objects.get(pk=pk)

    if post.author != request.user:
        return redirect('blog:post_detail', pk)

    if request.method == 'POST':
        post.delete()
        return redirect('blog:index')
    return render(request, 'blog/post_delete_confirm.html',{
        'post':post,
    })

@login_required
def comment_new(request,pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=pk)
            comment.author = request.user
            comment.save()
            return redirect('blog:post_detail', pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_forms.html',{
        'form':form,
    })

@login_required
def comment_edit(request, post_pk, pk):
    comment = Comment.objects.get(pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=post_pk)
            comment.save()
            return redirect('blog:post_detail', post_pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/post_forms.html',{
        'form':form,
    })
@login_required
def comment_delete(request, post_pk, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('blog:post_detail', post_pk)
    return render(request, 'blog/comment_delete_confirm.html',{
        'comment':comment,
    })



