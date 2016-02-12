from django.http import *
from django.shortcuts import render_to_response,redirect, render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .forms import SearchNameForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def antmain(request):
    # posts = Photo.objects.all().order_by('published_date')
    return render(request, 'admin-html/index.html',)
