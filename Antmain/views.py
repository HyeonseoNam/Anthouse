from django.http import *
from django.shortcuts import render_to_response,redirect, render
from django.template import RequestContext
from .models import Photo
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from Antmain.forms import SignupForm ,PhotoEditForm

def single_photo(request, photo_id):
    return HttpResponse('{0}번 사진입니다'.format(photo_id))

def post_list(request):
    posts = Photo.objects.all().order_by('published_date')
    return render(request, 'admin-html/index.html', {'posts' : posts})

def test_page(request):
    return render(request, 'photo/test.html',  )

def register(request):
    return render(request, 'registration/signup.html',  )

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

def signup(request):
    if request.method == "POST":
        signupform = SignupForm(request.POST)
        if signupform.is_valid():
            user = signupform.save(commit=False)
            user.email = signupform.cleaned_data['email']
            user.save()

            return HttpResponseRedirect(
                reverse("signup_ok")
            )
    elif request.method =="GET":
            signupform = SignupForm()

    return render(request, "registration/signup.html", {
         "signupform": signupform,
    })

def new_photo(request):
    if request.method == "GET":
        edit_form = PhotoEditForm()
    elif request.method == "POST":
        edit_form = PhotoEditForm(request.POST, request.FILES)

        if edit_form.is_valid():
            new_photo = edit_form.save()

            return redirect(new_photo.get_absolute_url())

    return render(
        request,
        'photo/new_photo.html',
        {
            'form': edit_form,
        }
    )