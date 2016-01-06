from __future__ import unicode_literals
from django import forms
# from Antmain.models import Photo
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User

#
# class PhotoEditForm(forms.ModelForm):
#     class Meta:
#         model = Photo
#         # fields =  "__all__"
#         exclude = ('filtered_image_file', )