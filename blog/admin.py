from django.contrib import admin
from .models import Post,Comment, Timeline

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Timeline)
