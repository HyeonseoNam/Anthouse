from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm, PostForm, TimelineForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from sdata.models import Stock2, Stock_current


def test(request):
    post_list = Post.objects.all().order_by('-created_at')
    if request.method == 'POST':
        form = TimelineForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            # return redirect('blog:post_detail', post.pk)
    else:
        form = TimelineForm()
    return render(request, 'blog/test.html', {
        'post_list': post_list,
        'form':form,
    })




# def search_name(request):
#     # if request.method =="GET":
#         # s = Stock2.objects.get(s_name=request.GET['title'])
#     s2 = Stock_current.objects.get(hname=request.POST.get('title'))
#
#     return render(request, "blog/test.html", {
#          # "searchform": searchform,
#         # 's_name' : s.s_name,
#         # 's_code' : s.s_code,
#         's2' : s2,})


# class StockListView(ListView):
#     model =  Stock_current
#     template_name = 'blog/test.html'
#     context_object_name = 'stock_list'
#
#
class StockDetailView(DetailView):
    model =  Stock_current
    template_name = 'blog/test.html'
    context_object_name = 's2'

    def get(self, request):
        s2 = Stock_current.objects.get(hname=request.GET['title'])

        return render(request, "blog/test.html", {
        's2' : s2,})






class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'

#
#
# def index(request):
#     post_list = Post.objects.all()
#     return render(request, 'blog/index.html', {
#         'post_list': post_list,
#     })

# def post_detail(request, pk):
#     post= Post.objects.get(pk=pk)
#     return render(request, 'blog/post_detail.html', {
#         'post':post,
#     })

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'




# @login_required
# def post_create(request):
#
#     #request.GET
#     #request.POST
#     #request.FILES
#
#     #request.user =>
#     # django.contrib.auth.models.AnonymousUser 로그인 안됐을때 자동 할당
#     # django.contrib.auth.models.User  로그인 됐을때 자동 할당
#     #
#
#
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect('blog:post_detail', post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_forms.html',{
#         'form':form,
#     })



class PostCreateView(CreateView):
    model=Post
    form_class = PostForm
    template_name = 'blog/post_forms.html'

    # success_url = reverse_lazy('blog:post_detail')         포스트 성공시 리다이렉트 아레 get_success_url로 대체가능

    def form_valid(self,form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super(PostCreateView,self).form_valid(form)

    def get_success_url(self):
        # redirect('blog:post_detail', self.object.pk)   #HttpResponseRedirect
        # reverse('blog:post_detail', args=[self.object.pk], kwargs={})    #string


        return reverse('blog:post_detail', args=[self.object.pk])

# post_create = login_required(PostCreateView.as_view())

#
# @login_required
# def post_update(request,pk):
#     post = Post.objects.get(pk=pk)
#
# # 자기가 작성한 유저가 아니라 다른 유저가 로그인하면 수정 , 삭제 안되게 막는 2줄 코드 -> 포스트 디테일로 돌아오게 만듬
#     if post.author != request.user:
#         return redirect('blog:post_detail', pk)
#
#     if request.method == 'POST':
#         form = PostForm(request.POST,request.FILES, instance=post)
#         if form.is_valid():
#             post = form.save()
#             return redirect('blog:post_detail', post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_forms.html',{
#         'form':form,
#     })

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_forms.html'


    def get_success_url(self):
        return reverse('blog:post_detail', args=[self.object.pk])



# @login_required
# def post_delete(request, pk):
#     post =Post.objects.get(pk=pk)
#
#     if post.author != request.user:
#         return redirect('blog:post_detail', pk)
#
#     if request.method == 'POST':
#         post.delete()
#         return redirect('blog:index')
#     return render(request, 'blog/post_delete_confirm.html',{
#         'post':post,
#     })

# post_delete = login_required(DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:index'), template_name='blog/post_delete_confirm.html'))
# 위 한줄 로직은 유저가 같을때 로직 구현 안돼있음


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')
    template_name='blog/post_delete_confirm.html'
    def dispatch(self, request, *args, **kwargs):
        if self.get_object().author != request.user:
            return redirect('blog:post_detail', self.kwargs['pk'])
        return super(PostDeleteView, self).dispatch(request, *args, **kwargs)

post_delete = PostDeleteView.as_view()
#  장고가 1.9 일때 클래스에 로그인 믹스인 기능 할수있음 , 위에는 로그인 안돼있어도 바로 디테일뷰로 보내서 로그인페이지로 안감 로직수정이 필요


# @login_required
# def comment_new(request,pk):
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = Post.objects.get(pk=pk)
#             comment.author = request.user
#             comment.save()
#             return redirect('blog:post_detail', pk)
#     else:
#         form = CommentForm()
#     return render(request, 'blog/post_forms.html',{
#         'form':form,
#     })

class CommentNewView(LoginRequiredMixin,CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/post_forms.html'

    def form_valid(self,form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.save()
        return super(CommentNewView,self).form_valid(form)

    def get_success_url(self):
        # redirect('blog:post_detail', self.object.pk)   #HttpResponseRedirect
        # reverse('blog:post_detail', args=[self.object.pk], kwargs={})    #string

        return reverse('blog:post_detail', args=[self.object.pk])


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


