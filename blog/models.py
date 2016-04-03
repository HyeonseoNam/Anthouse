from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from sdata.models import Stock_current

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title= models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Timeline(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    stock = models.ForeignKey(Stock_current, blank=True, null=True)
    content = models.TextField()
    photo = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.PositiveIntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.content


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author

class Message(models.Model):
    user = models.ForeignKey(User)
    message = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(User)
    message = models.ForeignKey('Message')