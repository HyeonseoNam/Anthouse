from django.http import *
from django.shortcuts import render_to_response,redirect, render
from django.template import RequestContext
from sdata.models import Stock
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .forms import SearchNameForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#
# def single_photo(request, photo_id):
#     return HttpResponse('{0}번 사진입니다'.format(photo_id))
#
def antmain(request):
    # posts = Photo.objects.all().order_by('published_date')
    return render(request, 'admin-html/index.html',)
#
# def test_page(request):
#     return render(request, 'photo/test.html',  )
#
# def register(request):
#     return render(request, 'registration/signup.html',  )

# def login_user(request):
#     logout(request)
#     username = password = ''
#     if request.POST:
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect('/main/')
#     return render_to_response('photo/index.html', context_instance=RequestContext(request))

# def new_photo(request):
#     if request.method == "GET":
#         edit_form = PhotoEditForm()
#     elif request.method == "POST":
#         edit_form = PhotoEditForm(request.POST, request.FILES)
#
#         if edit_form.is_valid():
#             new_photo = edit_form.save()
#
#             return redirect(new_photo.get_absolute_url())
#
#     return render(
#         request,
#         'photo/new_photo.html',
#         {
#             'form': edit_form,
#         }
#     )

def search_name(request):
    # if request.method =="GET":
    #         searchform = SearchNameForm()
    # sdata= Stock.objects.get()
    s = Stock.objects.get(s_name=request.POST['title'])

    return render(request, "../../blog/templates/blog/test.html", {
         # "searchform": searchform,
        's_name' : request.POST['title'],
        's_code' : s.s_code
    # if Stock.objects.get(s_code=request.POST['title']) != 'Null':
    #     return HttpResponse('%s' %Stock.objects.get(s_code=request.POST['title']))
    # else :
    #     return HttpResponse('실패')


     })

# class StockTitleView(ListView):
#     model = Stock
#     template_name = 'admin-html/blank.html'
#     context_object_name = 'stock_list'
#
# search = StockTitleView.as_view()