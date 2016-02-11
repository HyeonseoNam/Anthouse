from __future__ import unicode_literals
from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from sdata.models import Stock2



class SearchNameForm(forms.ModelForm):
    class Meta:
        model = Stock2
        # fields =  "__all__"
        fields = ("s_name","s_code")