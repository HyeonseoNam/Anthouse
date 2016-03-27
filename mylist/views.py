from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from accounts.models import Userprofile


# def mylist(request):
#     return render(request, 'mylist/mylist.html', {
#     })


class MyListView(ListView):
    model = Userprofile
    template_name = 'mylist/mylist.html'

    def get(self,request):
        matchuser = Userprofile.objects.get(user= self.request.user)
        stock_list= matchuser.stock.all()

        return render(request, "mylist/mylist.html", {'stock_list': stock_list})