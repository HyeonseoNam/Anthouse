from django.conf.urls import include, url , patterns
from . import views

urlpatterns = patterns('',
    url(r'^$', views.post_list, name='post_list'),
    # url(r'^test/$', views.test_page, name='test_page'),
    # url(r'^photo/(?P<photo_id>\d+)$', 'Antmain.views.single_photo', name='view_single_photo'),
    # url(r'^photo/upload/$', 'Antmain.views.new_photo', name='new_photo'),
)
