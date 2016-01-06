from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^(?P<pk>\d+)/$', 'blog.views.post_detail'),
    url(r'^(?P<pk>\d+)/comments/new/$', 'blog.views.comment_new'), #새 댓글생성
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', 'blog.views.comment_edit'), #댓글 수정



    url(r'^new/$', 'blog.views.post_new'),
]


# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
