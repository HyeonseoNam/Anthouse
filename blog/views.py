from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from .models import Post, Comment, Timeline
from .forms import CommentForm, PostForm, TimelineForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from sdata.models import Stock2, Stock_current
import json


def search_titles(request):
    if request.method == "POST":
        search_text = request.POST.get('search_text')
    else:
        search_text = ''

    articles = Stock_current.objects.filter(hname__contains = search_text)

    return render_to_response('blog/test2.html',{'articles':articles})

def EnemyAbility(request, tag=None):

    entries = Stock_current.objects.get(shcode=str(tag));

    data = entries.dic()

    return HttpResponse(json.dumps(data), content_type="application/json" )


# def timeline(request):
#     timeline_list = Timeline.objects.all().order_by('-created_at')
#     if request.method == 'POST':
#         form = TimelineForm(request.POST, request.FILES)
#         # shcode = request.POST.get('shcode')
#         shcode = '099220'
#         stock = Stock_current.objects.get(shcode=shcode)
#         if form.is_valid():
#             timeline = form.save(commit=False)
#             timeline.author = request.user
#             timeline.stock = stock
#             timeline.save()
#             # return redirect('blog:post_detail', post.pk)
#     else:
#         form = TimelineForm()
#     return render(request, 'blog/stock_detail.html', {
#         'timeline_list': timeline_list,
#         'form':form,
#     })


# 전체에서 글 작성기능은 기능은 안됨 , 임시구현
class StockListView(DetailView):
    model = Stock_current
    template_name = 'blog/timeline.html'
    context_object_name = 's2'

    def get(self, request):
        timeline_list = Timeline.objects.all().order_by('-created_at')

        context = {
            'timeline_list': timeline_list
        }

        return render(request, "blog/timeline.html", context)


# 종목 검색했을때 해당 페이지
class StockDetailView(DetailView):
    model = Stock_current
    template_name = 'blog/stock_detail.html'
    context_object_name = 's2'


    def get(self, request):
        # s2 = Stock_current.objects.get(hname=request.GET.get('title'))
        search = request.GET.get('search')

        try:
            int(search)
            search_value = search
            s2 = Stock_current.objects.get(shcode=search_value)
        except:
            # 숫자가 아닐때 shcode 가 정의가 되지 않아서 에러가 남.
            str(search)
            search_value = search
            s2 = Stock_current.objects.get(hname=search_value)

        timeline_list = Timeline.objects.filter(stock=s2).order_by('-created_at')

        context = {
            's2': s2,
            'search_value': search_value,
            'timeline_list': timeline_list
        }

        return render(request, "blog/stock_detail.html", context)

    def post(self,request):
        form = TimelineForm(request.POST, request.FILES)
        search_value = request.POST.get('search_value')

        try:
            int(search_value)
            s2 = Stock_current.objects.get(shcode=search_value)
        except:
            str(search_value)
            s2 = Stock_current.objects.get(hname=search_value)

        if form.is_valid():
            timeline = form.save(commit=False)
            timeline.author = request.user
            timeline.stock = s2
            timeline.save()

        timeline_list = Timeline.objects.filter(stock=s2).order_by('-created_at')


        return render(request, 'blog/stock_detail.html', {
            's2': s2,
            'timeline_list': timeline_list,
            'form':form,
        })




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


# class TimelineCreateView(CreateView):
#     model = Timeline
#     form_class = CommentForm
#     template_name = 'blog/post_forms.html'
#
#     def form_valid(self,form):
#         comment = form.save(commit=False)
#         comment.author = self.request.user
#         comment.save()
#         return super(CommentNewView,self).form_valid(form)
#
#     def get_success_url(self):
#         # redirect('blog:post_detail', self.object.pk)   #HttpResponseRedirect
#         # reverse('blog:post_detail', args=[self.object.pk], kwargs={})    #string
#
#         return reverse('blog:post_detail', args=[self.object.pk])

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


