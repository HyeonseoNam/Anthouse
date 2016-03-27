from django.conf.urls import url, patterns
from mylist.views import MyListView



urlpatterns = patterns('mylist.views',

    # url(r'^$', 'mylist', name='mylist'),
    url(r'^$', MyListView.as_view(), name='mylist'),

    )