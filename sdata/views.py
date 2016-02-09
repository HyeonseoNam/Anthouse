from django.shortcuts import render, redirect
from .models import Stock2, Stock_current
# from .forms import CommentForm, PostForm, TimelineForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class StockListView(ListView):
    model = Stock2
    template_name = 'sdata/data_view.html'
    context_object_name = 'stock_list'

data_test = StockListView.as_view()

class StockCurrentVIew(ListView):
    model = Stock_current
    template_name = 'sdata/data_current_view.html'
    context_object_name = 'stock_current_list'