from django.shortcuts import render, redirect
from .models import Stock
# from .forms import CommentForm, PostForm, TimelineForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class StockListView(ListView):
    model = Stock
    template_name = 'sdata/data_view.html'
    context_object_name = 'stock_list'

data_test = StockListView.as_view()