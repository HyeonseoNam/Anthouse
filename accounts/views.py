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