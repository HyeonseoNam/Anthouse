from django.conf.urls import url, patterns



urlpatterns = patterns('chart.views',

    url(r'^$', 'chart', name='chart'),

    )