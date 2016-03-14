from django.http import *
from django.shortcuts import render_to_response,redirect, render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from accounts.forms import SignupForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserProfileForm
from .models import Userprofile, User

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


class UserProfileView(DetailView):
    model = Userprofile
    template_name = 'accounts/profile.html'
    context_object_name = 'userlist'



    def get(self, request, *args, **kwargs):
        # s2 = Stock_current.objects.get(hname=request.GET.get('title'))
        search = request.GET.get('search')


        userlist = Userprofile.objects.get(nickname = "카이타샤")

        context = {
            'userlist': userlist,
        }
        return render(request, "accounts/profile.html", context)

    # def post(self,request):
    #     form = UserProfileForm(request.POST, request.FILES)
    #     # name = request.POST.get('name')
    #     # nickname = request.POST.get('nickname')
    #     # email = request.POST.get('photo')
    #     # photo = request.POST.get('photo')
    #     #
    #     if form.is_valid():
    #         userlist = form.save(commit=False)
    #         userlist.user = request.user
    #         userlist.save()
    #
    #     # timeline_list = Timeline.objects.filter(stock=s2).order_by('-created_at')
    #
    #
    #     return render(request, 'accounts/profile.html', {
    #         'userlist': userlist,
    #         'form':form,
    #     })
