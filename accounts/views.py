from django.http import *
from django.shortcuts import render_to_response,redirect, render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from accounts.forms import SignupForm
# Create your views here.


def signup(request):
    if request.method == "POST":
        signupform = SignupForm(request.POST)
        if signupform.is_valid():

            user = signupform.save()
            # user = signupform.save(commit=False)
            # user.email = signupform.cleaned_data['email']
            user.save()

            return redirect("signup_ok")

    elif request.method =="GET":
            signupform = SignupForm()

    return render(request, "registration/signup.html", {
         "signupform": signupform,
    })



# class PostCreateView(CreateView):
#     model=Post
#     form_class = PostForm
#     template_name = 'blog/post_forms.html'
#
#     # success_url = reverse_lazy('blog:post_detail')         포스트 성공시 리다이렉트 아레 get_success_url로 대체가능
#
#     def form_valid(self,form):
#         post = form.save(commit=False)
#         post.author = self.request.user
#         post.save()
#         return super(PostCreateView,self).form_valid(form)
#
#     def get_success_url(self):
#         # redirect('blog:post_detail', self.object.pk)   #HttpResponseRedirect
#         # reverse('blog:post_detail', args=[self.object.pk], kwargs={})    #string
#
#
#         return reverse('blog:post_detail', args=[self.object.pk])
#
# post_create = login_required(PostCreateView.as_view())