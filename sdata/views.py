from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Stock2, Stock_current
# from .forms import CommentForm, PostForm, TimelineForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import json


class StockListView(ListView):
    model = Stock2
    template_name = 'sdata/data_view.html'
    context_object_name = 'stock_list'

data_test = StockListView.as_view()

class StockCurrentVIew(ListView):
    model = Stock_current
    template_name = 'sdata/data_current_view.html'
    context_object_name = 'stock_current_list'


def stock_data(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        drugs = Stock_current.objects.filter(hname__icontains = q )[:20]
        results = []
        for drug in drugs:
            drug_json = {}
            drug_json['title'] = drug.hname
            drug_json['text'] = drug.shcode
            # drug_json['value'] = drug.hanme
            results.append(drug_json)
        pages = json.dumps(results)
    else:
        pages = 'fail'
    mimetype = 'application/json'
    return HttpResponse(pages, mimetype)