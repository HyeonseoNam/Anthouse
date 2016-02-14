from django.contrib import admin
from .models import Post,Comment, Timeline, Message,Like

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Timeline)
admin.site.register(Message)
admin.site.register(Like)
