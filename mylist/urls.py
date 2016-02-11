from django.conf.urls import url, patterns



urlpatterns = patterns('mylist.views',

    url(r'^$', 'mylist', name='mylist'),

    )