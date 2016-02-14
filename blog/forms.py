from django import forms
from .models import Comment, Post, Timeline


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields ='__all__'
        fields =('title','content','photo')

class TimelineForm(forms.ModelForm):
    class Meta:
        model = Timeline
        fields = ('content','photo')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ('message',)
        exclude = ()