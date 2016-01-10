from django.conf.urls import include, url, patterns
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('blog.views',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<pk>\d+)/$', 'post_detail', name='post_detail'),
    url(r'^new/$', 'post_create', name='post_create'),

    url(r'^test/$', 'test', name='post_test'),
    url(r'^(?P<pk>\d+)/edit/$', 'post_update', name='post_update'),

    url(r'^(?P<pk>\d+)/delete/$', 'post_delete', name='post_delete'),


    url(r'^(?P<pk>\d+)/comments/new/$', 'comment_new', name='comment_new'), #새 댓글생성
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', 'comment_edit', name='comment_edit'), #댓글 수정
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/delete/$', 'comment_delete', name='comment_delete'), #댓글 삭제




    )


# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
